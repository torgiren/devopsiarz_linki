Redis
------
https://redis.io/download

download, compile, run src/redis-server
(5 minutes total)

Virtualenv
-----------

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Linker
------

```
python linker.py
```


Usage
-----

Set some links:

```
$ curl localhost:8080/set -X POST -d "target=http://onet.pl" -d "site=yt"
new: c01ad
curl localhost:8080/set -X POST -d "target=http://wp.pl" -d "site=yt"
new: 5f3a1
$ curl localhost:8080/set -X POST -d "target=http://onet.pl" -d "site=wykop"
new: 80d99
$ curl localhost:8080/set -X POST -d "target=http://onet.pl" -d "site=kwejk"
new: c8962
```

list links

```
$ curl localhost:8080/list
5f3a1, b'http://wp.pl', b'yt', None
c01ad, b'http://onet.pl', b'yt', None
80d99, b'http://onet.pl', b'wykop', None
c8962, b'http://onet.pl', b'kwejk', None
```

Use some links:

```
$ curl localhost:8080/get/c01ad -I
HTTP/1.0 303 See Other
Date: Wed, 05 Aug 2020 21:29:40 GMT
Server: WSGIServer/0.2 CPython/3.7.8
Location: http://onet.pl
Content-Length: 0
Content-Type: text/html; charset=UTF-8

$ curl localhost:8080/get/c01ad -I
HTTP/1.0 303 See Other
Date: Wed, 05 Aug 2020 21:29:42 GMT
Server: WSGIServer/0.2 CPython/3.7.8
Location: http://onet.pl
Content-Length: 0
Content-Type: text/html; charset=UTF-8

$ curl localhost:8080/get/c01ad -I
HTTP/1.0 303 See Other
Date: Wed, 05 Aug 2020 21:29:43 GMT
Server: WSGIServer/0.2 CPython/3.7.8
Location: http://onet.pl
Content-Length: 0
Content-Type: text/html; charset=UTF-8

$ curl localhost:8080/get/c8962 -I
HTTP/1.0 303 See Other
Date: Wed, 05 Aug 2020 21:29:50 GMT
Server: WSGIServer/0.2 CPython/3.7.8
Location: http://onet.pl
Content-Length: 0
Content-Type: text/html; charset=UTF-8
```

List again

```
$ curl localhost:8080/list
5f3a1, b'http://wp.pl', b'yt', None
80d99, b'http://onet.pl', b'wykop', None
c8962, b'http://onet.pl', b'kwejk', b'1'
c01ad, b'http://onet.pl', b'yt', b'3'
```

