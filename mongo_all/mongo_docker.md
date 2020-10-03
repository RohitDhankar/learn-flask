```
$ which docker
/usr/bin/docker
$ docker --version
Docker version 19.03.12, build 48a66213fe
$ sudo docker pull mongo
[sudo] password for dhankar: 
Using default tag: latest
latest: Pulling from library/mongo
171857c49d0f: Pull complete 
419640447d26: Pull complete 
61e52f862619: Pull complete 
892787ca4521: Pull complete 
06e2d54757a5: Pull complete 
e2f7d90822f3: Pull complete 
f518d3776320: Pull complete 
feb8e9d469d8: Pull complete 
69705b632494: Pull complete 
c7daea26376d: Pull complete 
13d1f9e1fc77: Pull complete 
f87e65fe7ffd: Pull complete 
Digest: sha256:a4448eb5f6e6097353d0ab97eb50aeb0238bb4e60c37e401920d3c2c4fc73eb9
Status: Downloaded newer image for mongo:latest
docker.io/library/mongo:latest
$ 
```
#

```
$ sudo docker ps
[sudo] password for dhankar: 
CONTAINER ID        IMAGE                        COMMAND                  CREATED             STATUS              PORTS                     NAMES
2c6b15fb1e0a        opendronemap/webodm_webapp   "/bin/bash -c 'chmod…"   2 months ago        Up 5 hours          0.0.0.0:8000->8000/tcp    webapp
9838404c3227        opendronemap/webodm_webapp   "/bin/bash -c '/webo…"   2 months ago        Up 5 hours                                    worker
bdf69c31808d        opendronemap/nodeodm         "/usr/bin/nodejs /va…"   2 months ago        Up 5 hours          0.0.0.0:32769->3000/tcp   webodm_node-odm_1
9f3d191805e5        opendronemap/webodm_db       "docker-entrypoint.s…"   2 months ago        Up 5 hours          0.0.0.0:32768->5432/tcp   db
b664208c5e60        redis                        "docker-entrypoint.s…"   2 months ago        Up 5 hours          6379/tcp                  broker
```

#
- FOOBAR - need to kill the - opendronemap - containers 
- 

sudo docker run -it -d mongo

```
$ sudo docker ps
CONTAINER ID        IMAGE                        COMMAND                  CREATED             STATUS              PORTS                     NAMES
6d0ffb3e4f61        mongo                        "docker-entrypoint.s…"   4 minutes ago       Up 4 minutes        27017/tcp                 jovial_bohr
2c6b15fb1e0a        opendronemap/webodm_webapp   "/bin/bash -c 'chmod…"   2 months ago        Up 5 hours          0.0.0.0:8000->8000/tcp    webapp
9f3d191805e5        opendronemap/webodm_db       "docker-entrypoint.s…"   2 months ago        Up 5 hours          0.0.0.0:32768->5432/tcp   db
b664208c5e60        redis                        "docker-entrypoint.s…"   2 months ago        Up 5 hours          6379/tcp                  broker
$ 
$ sudo docker stop webapp
webapp
$ sudo docker ps
CONTAINER ID        IMAGE                    COMMAND                  CREATED             STATUS              PORTS                     NAMES
6d0ffb3e4f61        mongo                    "docker-entrypoint.s…"   5 minutes ago       Up 5 minutes        27017/tcp                 jovial_bohr
9f3d191805e5        opendronemap/webodm_db   "docker-entrypoint.s…"   2 months ago        Up 5 hours          0.0.0.0:32768->5432/tcp   db
b664208c5e60        redis                    "docker-entrypoint.s…"   2 months ago        Up 5 hours          6379/tcp                  broker
$ sudo docker stop db
db
$ sudo docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
6d0ffb3e4f61        mongo               "docker-entrypoint.s…"   5 minutes ago       Up 5 minutes        27017/tcp           jovial_bohr
b664208c5e60        redis               "docker-entrypoint.s…"   2 months ago        Up 5 hours          6379/tcp            broker
$ 

```


