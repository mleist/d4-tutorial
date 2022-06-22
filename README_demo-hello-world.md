# d4 - Hello World Tutorial

This tutorial introduces a very simple application of d4.

1st Steps - see README.md


## 1. get d4 tutorial

```bash
$ git clone https://github.com/mleist/d4-tutorial.git
$ cd d4-tutorial/
```


## 2. create new hello world (optional)

```bash
$ cruft create \
    --no-input \
    --skip envs \
    --config-file cookiecutter-demo-hello-world.yaml \
    --output-dir . \
    https://github.com/mleist/d4/
 [SUCCESS]: Project initialized, keep up the good work!
```


## 3. start hello world example

```bash
$ cd demo-hello-world/
$ cp dotenv.dist .env
$ cp -a envs.dist envs
$ docker-compose --file docker-compose-local.yml build --no-cache
$ docker-compose --file docker-compose-local.yml down
$ docker-compose --file docker-compose-local.yml up -d
```


## 4. testing ...

```bash
$ curl -v "http://127.0.0.1:9020/"
*   Trying 127.0.0.1:9020...
* Connected to 127.0.0.1 (127.0.0.1) port 9020 (#0)
> GET / HTTP/1.1
> Host: 127.0.0.1:9020
> User-Agent: curl/7.83.1
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< date: [...]
< server: uvicorn
< content-length: 38
< content-type: application/json
<
* Connection #0 to host 127.0.0.1 left intact
{"msg":"success","text":"hello world"}⏎
```


## 4. ... measuring

```bash
$ ab -n 3000 -c 25 "http://127.0.0.1:9020/"
[...]
```
