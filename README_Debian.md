# d4 - Example for a d4 debian system

> long Version:
> 
> https://docs.docker.com/engine/install/debian/

> user login with sudo permission

### update the system

```bash
sudo apt-get update
```

```bash
sudo apt-get install --assume-yes \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg \
        lsb-release
```

### configure docker repo

```bash
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```


```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### install docker + tools

```bash
sudo apt-get update
```


```bash
sudo apt-get install --assume-yes docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

> Attention: read the docu first:

```bash
sudo usermod -aG docker $USER
```

Log out and log back in 

### Ok, ready with docker

```bash
user@debian:~$ docker --version
Docker version 20.10.16, build aa7e414
```

```bash
user@debian:~$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

### Creating the preconditions for d4

```bash
sudo apt-get install --assume-yes python3-venv
```
