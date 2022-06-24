# d4 - Proxy Tutorial

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
    --config-file ./cookiecutter-demo-proxy.yaml \
    --output-dir . \
    https://github.com/mleist/d4/
 [SUCCESS]: Project initialized, keep up the good work!
```


## 3. start TLS-Proxy example

```bash
$ cd demo-proxy
$ cp dotenv.dist .env
$ cp -a envs.dist envs
```

Please adjust the environment

```bash
$ proxy/init-letsencrypt.sh
```
