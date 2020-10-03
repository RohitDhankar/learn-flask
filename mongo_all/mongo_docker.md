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
#

```
$ sudo docker images #Listing all images on this system
[sudo] password for dhankar: 
REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
mongo                        latest              ba0c2ff8d362        7 days ago          492MB
opendronemap/webodm_webapp   latest              96e495184451        2 months ago        2.77GB
opendronemap/nodeodm         latest              735a7085ce6a        2 months ago        3.61GB
redis                        latest              235592615444        3 months ago        104MB
hello-world                  latest              bf756fb1ae65        9 months ago        13.3kB
opendronemap/webodm_db       latest              7cf185d87821        3 years ago         609MB

```
#
```
$ sudo docker ps -a
CONTAINER ID        IMAGE                        COMMAND                  CREATED             STATUS                     PORTS               NAMES
6d0ffb3e4f61        mongo                        "docker-entrypoint.s…"   2 hours ago         Up 2 hours                 27017/tcp           jovial_bohr
2c6b15fb1e0a        opendronemap/webodm_webapp   "/bin/bash -c 'chmod…"   2 months ago        Exited (137) 2 hours ago                       webapp
9838404c3227        opendronemap/webodm_webapp   "/bin/bash -c '/webo…"   2 months ago        Exited (137) 2 hours ago                       worker
bdf69c31808d        opendronemap/nodeodm         "/usr/bin/nodejs /va…"   2 months ago        Exited (0) 2 hours ago                         webodm_node-odm_1
9f3d191805e5        opendronemap/webodm_db       "docker-entrypoint.s…"   2 months ago        Exited (0) 2 hours ago                         db
b664208c5e60        redis                        "docker-entrypoint.s…"   2 months ago        Up 8 hours                 6379/tcp            broker
c0c514eee9ed        hello-world                  "/hello"                 2 months ago        Exited (0) 2 months ago                        determined_fermi

```
#
```
$ sudo docker exec -it jovial_bohr bash
[sudo] password for dhankar: 
root@6d0ffb3e4f61:/# 
root@6d0ffb3e4f61:/# ls
bin   data  docker-entrypoint-initdb.d  home        lib    media  opt   root  sbin  sys  usr
boot  dev   etc                         js-yaml.js  lib64  mnt    proc  run   srv   tmp  var
root@6d0ffb3e4f61:/# 

```
#
root@6d0ffb3e4f61:/# mongo
MongoDB shell version v4.4.1
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("31b82067-c6e3-4845-b67b-a343992f0356") }
MongoDB server version: 4.4.1
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
	https://docs.mongodb.com/
Questions? Try the MongoDB Developer Community Forums
	https://community.mongodb.com
---
The server generated these startup warnings when booting: 
        2020-10-03T12:04:49.738+00:00: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
        2020-10-03T12:04:51.006+00:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
---
---
        Enable MongoDB's free cloud-based monitoring service, which will then receive and display
        metrics about your deployment (disk utilization, CPU, operation statistics, etc).

        The monitoring data will be available on a MongoDB website with a unique URL accessible to you
        and anyone you share the URL with. MongoDB may use this information to make product
        improvements and to suggest MongoDB products and deployment options to you.

        To enable free monitoring, run the following command: db.enableFreeMonitoring()
        To permanently disable this reminder, run the following command: db.disableFreeMonitoring()
---
> 
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> 
> use flask_test
switched to db flask_test
> 
```
```
#
```
```
#

#
```
```
#
```
```
#

#
```
```
#
```
```
#


#
```
```
#
```
```
#




