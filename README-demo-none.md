# d4 - "None" project

If all features are switched off, an empty directory structure should be generated.

1st Steps - see README.md

## get d4 tutorial

```bash
$ git clone https://github.com/mleist/d4-tutorial.git
$ cd d4-tutorial/
```


```bash
$ cruft create \
    --no-input \
    --skip envs \
    --config-file ./cookiecutter-demo-none.yaml \
    --output-dir . \
    https://github.com/mleist/d4/
 [SUCCESS]: Project initialized, keep up the good work!
```

```bash
$ ls -R1a demo-none/
./
../
.cruft.json
.env
.gitignore
.pylintrc
__init__.py
cookiecutter-config-file.yml
docker-compose-local.yml
docker-compose-production.yml
dotenv.dist
scripts/

demo-none//scripts:
./
../
test.sh*
```
