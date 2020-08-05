#!/usr/bin/env python
import redis
from bottle import route, run, template, redirect, abort, post, request
import json
import hashlib
r = redis.Redis(host='localhost', port=6379, db=0)


@route('/get/<name>')
def get_link(name):
    link = r.get(name+"_target")
    if not link:
        abort(404)
    r.incr(name+"_counter")
    redirect(link.decode())

@route('/list')
def list_links():
    result = []
    for i in r.keys("*_target"):
        link = i.decode().split("_target")[0]
        target = r.get(i)
        site = r.get(link+"_site")
        counter = r.get(link+"_counter")
        result.append("{link}, {target}, {site}, {counter}".format(link=link,target=target,site=site, counter=counter))
    return "\n".join(result)+"\n"

@post('/set')
def set():
    target = request.forms.get("target").encode()
    site = request.forms.get("site","none").encode()
    h = hashlib.md5(target)
    for i in r.keys("*_target"):
        link = i.decode().split("_target")[0]
        if r.get(i)== target and r.get(link+"_site") == site:
            return "exists: " + link

    while (h.hexdigest()[:5]+"_target").encode() in r.keys():
        h = hashlib.md5(h.hexdigest().encode())
    link = h.hexdigest()[:5]
    r.set(link+"_target", target)
    r.set(link+"_site", site)
    return "new: " + link

run(host='localhost', port=8080)

