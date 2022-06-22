# d4 - Tutorial

d4-tutorial provides an application of d4 to learn how to use [d4](https://github.com/mleist/d4). 

## 1st Steps - how to use it in a virtual python environment.

### optionally create a virtual environment like

```bash
$ mkdir ~/.virtualenvs
$ python3 -m venv ~/.virtualenvs/d4-tutorial
$ source ~/.virtualenvs/d4-tutorial/bin/activate[.fish|.csh]
$ pip --version
pip 22.0.2 from [...]/d4-tutorial/lib/python3.10/site-packages/pip (python 3.10)
```

### Next steps

```bash
$ pip install --upgrade pip
[...]
$ pip install cruft
[...]

$ cruft --help
Usage: cruft [OPTIONS] COMMAND [ARGS]...

  _____________________________________________/\\\\\___________________
  ____________________________________________/\\\///___________________
  ____________________________________________/\\\________/\\\__________
  ___/\\\\\\\\__/\\/\\\\\\\___/\\\____/\\\__/\\\\\\\\\__/\\\\\\\\\\\____
  __/\\\//////__\/\\\/////\\\_\/\\\___\/\\\_\////\\\//__\////\\\////____
  __/\\\_________\/\\\___\///__\/\\\___\/\\\____\/\\\_______\/\\\_______
  __\//\\\________\/\\\_________\/\\\___\/\\\____\/\\\_______\/\\\_/\\__
  ____\///\\\\\\\\_\/\\\_________\//\\\\\\\\\_____\/\\\_______\//\\\\\__
  _______\////////__\///___________\/////////______\///_________\/////__

  If you need the boilerplate, at least let cruft manage it.

  Version: 2.10.2

  Copyright Timothy Edmund Crosley, Sambhav Kothari 2020 MIT License

Options:
  --help  Show this message and exit.

Commands:
  check   Check if the linked Cookiecutter template has been updated
  create  Create a new project from a Cookiecutter template
  diff    Show the diff between the project and the current cruft template.
  link    Link an existing project to a Cookiecutter template
  update  Update the project to the latest version of the linked Cookiecutter
          template
```

```bash
$ cruft create --help
Usage: cruft create [OPTIONS] TEMPLATE

  Expand a Git based Cookiecutter template into a new project on disk.

Arguments:
  TEMPLATE  The Cookiecutter template URI.  [required]

Options:
  --output-dir DIRECTORY     Where to output the generated project dir into
                             [default: .]
  --config-file PATH         Path to the Cookiecutter user config file
  -d, --default-config       Do not load a config file. Use the defaults
                             instead
  --extra-context TEXT       A JSON string describing any extra context to
                             pass to cookiecutter.
  -y, --no-input             Do not prompt for parameters and only use
                             cookiecutter.json file content
  --directory TEXT           Directory within repo that holds
                             cookiecutter.json file for advanced repositories
                             with multi templates in it
  -c, --checkout TEXT        The git reference to check against. Supports
                             branches, tags and commit hashes.
  -f, --overwrite-if-exists  Overwrite the contents of the output directory if
                             it already exists
  --skip TEXT                Default files/pattern to skip on update
  --help                     Show this message and exit.
```

```bash
$ git clone https://github.com/mleist/d4-tutorial.git
$ cd d4-tutorial/
```


### Documentation

```bash
$ cruft create    --no-input \
                  --skip envs \
                  --config-file cookiecutter-demo-doc.yaml \
                  --output-dir . \
                  https://github.com/mleist/d4/
 [SUCCESS]: Project initialized, keep up the good work!
```

```bash
$ ls -1 demo-docs/docs/
01_very_first_tests.md
02_first_docker_compose.md
03_first_testing_infrastructure.md
04_build_test_companies.md
```



### Tests

```bash
$ cruft create    --no-input \
                  --skip envs \
                  --config-file cookiecutter-demo-tests.yaml \
                  --output-dir . \
                  https://github.com/mleist/d4/
 [SUCCESS]: Project initialized, keep up the good work!
```

```bash
$ cd demo-tests/
$ pytest .
[...]
collecting ...
 adapter/tests/test_01.py ✓
 tests/adapter/auth/test_01.py ✓✓✓
 tests/adapter/base/test_01.py ✓
 tests/spot/auth/test_01.py ✓✓
 tests/spot/base/test_01.py ✓✓

Results (54.12s):
       9 passed
```



### First SPOT Demo

```bash
$ cruft create --no-input \
                                              --skip envs \
                                              --config-file cookiecutter-demo-location-spot.yaml \
                                              --output-dir . \
                                              https://github.com/mleist/d4/
 [SUCCESS]: Project initialized, keep up the good work!
```

```bash
$ cd demo-location-spot/
$ docker-compose --file docker-compose-local.yml up -d
$ docker-compose --file docker-compose-local.yml up -d
[...]
[+] Running 5/5
 ⠿ Network demo-location-spot_default       Created                                                                                                                                                                                0.0s
 ⠿ Container demo-location-spot-keycloak-1  Started                                                                                                                                                                                0.7s
 ⠿ Container demo-location-spot-postgres-1  Started                                                                                                                                                                                0.7s
 ⠿ Container demo-location-spot-opa-1       Started                                                                                                                                                                                1.2s
 ⠿ Container demo-location-spot-spot-1      Started
[...]
```


```bash
$ curl -s -v http://localhost:9040/ >/dev/null
*   Trying 127.0.0.1:9040...
* Connected to localhost (127.0.0.1) port 9040 (#0)
> GET / HTTP/1.1
> Host: localhost:9040
> User-Agent: curl/7.82.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< date: Fri, 29 Apr 2022 16:35:12 GMT
< server: uvicorn
< content-type: text/html; charset=utf-8
< server-timing: TimerPanel_utime;dur=132.2669999999999;desc="User CPU time", TimerPanel_stime;dur=2.920999999999979;desc="System CPU time", TimerPanel_total;dur=135.1879999999999;desc="Total CPU time", TimerPanel_total_time;dur=144.7927951812744;desc="Elapsed time", SQLPanel_sql_time;dur=0;desc="SQL 0 queries", CachePanel_total_time;dur=0;desc="Cache 0 Calls"
< x-frame-options: DENY
< vary: Cookie, Accept-Language
< content-length: 122179
< content-language: en
< x-content-type-options: nosniff
< x-xss-protection: 1; mode=block
< referrer-policy: same-origin
< set-cookie: csrftoken=kybWHqtTKKeupzPhqfYFrNQnv14rokLaeM8uMDJ1bWagGteRvxyhbM1AmhrZe1mu; expires=Fri, 28 Apr 2023 16:35:13 GMT; HttpOnly; Max-Age=31449600; Path=/; SameSite=Lax
<
{ [23768 bytes data]
* Connection #0 to host localhost left intact

```
