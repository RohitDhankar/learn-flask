- MongoDB install on Ubuntu 18 
- https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

```
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
[sudo] password for dhankar: 
OK
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ touch /etc/apt/sources.list.d/mongodb-org-4.4.list
touch: cannot touch '/etc/apt/sources.list.d/mongodb-org-4.4.list': Permission denied
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ sudo touch /etc/apt/sources.list.d/mongodb-org-4.4.list
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ cd /etc/apt/sources.list.d/mongodb-org-4.4.list
bash: cd: /etc/apt/sources.list.d/mongodb-org-4.4.list: Not a directory
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ cd /etc/apt/sources.list.d/
(base) dhankar@dhankar-1:/etc/apt/sources.list.d$ ls -ltr
total 100
-rw-r--r-- 1 root root 193 Jul 30 11:51 slack.list.save
-rw-r--r-- 1 root root 126 Jul 30 11:51 mixxx-ubuntu-mixxx-bionic.list.save
-rw-r--r-- 1 root root 114 Jul 30 11:51 kxstudio-external.list.save
-rw-r--r-- 1 root root 162 Jul 30 11:51 cybermax-dexter-ubuntu-sdl2-backport-bionic.list.save
-rw-r--r-- 1 root root 166 Jul 30 11:51 apandada1-ubuntu-brightness-controller-bionic.list.save
-rw-r--r-- 1 root root  56 Jul 30 11:51 skype-stable.list.save
-rw-r--r-- 1 root root 193 Jul 30 11:51 vscode.list.save
-rw-r--r-- 1 root root 160 Jul 30 11:51 ubuntugis-ubuntu-ubuntugis-unstable-bionic.list.save
-rw-r--r-- 1 root root  51 Jul 30 11:51 ros-latest.list.save
-rw-r--r-- 1 root root 740 Jul 30 11:51 kxstudio-debian-ppas.list.save
-rw-r--r-- 1 root root 189 Jul 30 11:51 google-chrome.list.save
-rw-r--r-- 1 root root  50 Jul 30 11:51 cuda-ubuntu1804-11-0-local.list.save
-rw-r--r-- 1 root root 193 Jul 30 11:51 slack.list
-rw-r--r-- 1 root root 126 Jul 30 11:51 mixxx-ubuntu-mixxx-bionic.list
-rw-r--r-- 1 root root 162 Jul 30 11:51 cybermax-dexter-ubuntu-sdl2-backport-bionic.list
-rw-r--r-- 1 root root 166 Jul 30 11:51 apandada1-ubuntu-brightness-controller-bionic.list
-rw-r--r-- 1 root root 193 Jul 30 11:51 vscode.list
-rw-r--r-- 1 root root 160 Jul 30 11:51 ubuntugis-ubuntu-ubuntugis-unstable-bionic.list
-rw-r--r-- 1 root root  56 Jul 30 11:51 skype-stable.list
-rw-r--r-- 1 root root  51 Jul 30 11:51 ros-latest.list
-rw-r--r-- 1 root root 114 Jul 30 11:51 kxstudio-external.list
-rw-r--r-- 1 root root 740 Jul 30 11:51 kxstudio-debian-ppas.list
-rw-r--r-- 1 root root 189 Jul 30 11:51 google-chrome.list
-rw-r--r-- 1 root root  50 Jul 30 11:51 cuda-ubuntu1804-11-0-local.list
-rw-r--r-- 1 root root 142 Jul 30 11:51 alexlarsson-ubuntu-flatpak-bionic.list
-rw-r--r-- 1 root root   0 Sep 24 08:58 mongodb-org-4.4.list
(base) dhankar@dhankar-1:/etc/apt/sources.list.d$ 
(base) dhankar@dhankar-1:/etc/apt/sources.list.d$ cd -
/home/dhankar/temp/flask/learn-flask
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ sudo apt-get update
Get:1 file:/var/cuda-repo-ubuntu1804-11-0-local  InRelease
Ign:1 file:/var/cuda-repo-ubuntu1804-11-0-local  InRelease
Get:2 file:/var/cuda-repo-ubuntu1804-11-0-local  Release [564 B]
Get:2 file:/var/cuda-repo-ubuntu1804-11-0-local  Release [564 B]
Hit:4 https://dl.winehq.org/wine-builds/ubuntu bionic InRelease                             
Hit:7 https://repo.skype.com/deb stable InRelease                                                                       
Get:5 https://qgis.org/ubuntugis bionic InRelease [3,699 B]                                                                                  
Err:5 https://qgis.org/ubuntugis bionic InRelease                                                                                           
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY F7E06F06199EF2F2
Get:6 https://qgis.org/ubuntu bionic InRelease [3,699 B]                                                                            
Err:6 https://qgis.org/ubuntu bionic InRelease                                                                                              
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY F7E06F06199EF2F2
Hit:8 http://in.archive.ubuntu.com/ubuntu bionic InRelease                                                                          
Get:9 http://in.archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]                                                         
Get:10 http://in.archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]                                                      
Get:11 http://in.archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages [1,088 kB]                                
Hit:12 http://dl.google.com/linux/chrome/deb stable InRelease                                                            
Get:13 http://in.archive.ubuntu.com/ubuntu bionic-updates/main i386 Packages [747 kB]                                    
Get:14 http://in.archive.ubuntu.com/ubuntu bionic-updates/main amd64 DEP-11 Metadata [295 kB]                            
Get:15 http://in.archive.ubuntu.com/ubuntu bionic-updates/universe i386 Packages [1,034 kB]                                      
Get:16 http://in.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 Packages [1,114 kB]                               
Get:17 http://in.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 DEP-11 Metadata [285 kB]
Get:18 http://in.archive.ubuntu.com/ubuntu bionic-updates/multiverse amd64 DEP-11 Metadata [2,468 B] 
Get:19 http://in.archive.ubuntu.com/ubuntu bionic-backports/universe amd64 DEP-11 Metadata [9,288 B]
Get:20 https://deb.torproject.org/torproject.org bionic InRelease [4,244 B]                                                                  
Err:20 https://deb.torproject.org/torproject.org bionic InRelease                                      
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 74A941BA219EC810
Get:21 http://packages.microsoft.com/repos/vscode stable InRelease [3,959 B]                   
Ign:22 https://kx.studio/repo stable InRelease                                                                                               
Get:23 http://packages.microsoft.com/repos/vscode stable/main amd64 Packages [200 kB]                                                        
Ign:24 https://kx.studio/repo gcc5 InRelease                                                                                                 
Hit:25 https://kx.studio/repo stable Release                                                                                                 
Hit:27 https://kx.studio/repo gcc5 Release                                                                                                   
Get:29 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]                                                                 
Get:30 http://security.ubuntu.com/ubuntu bionic-security/main amd64 DEP-11 Metadata [49.0 kB]                                                
Get:31 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 DEP-11 Metadata [56.0 kB]                                            
Get:32 http://security.ubuntu.com/ubuntu bionic-security/multiverse amd64 DEP-11 Metadata [2,464 B]                                          
Get:34 https://download.docker.com/linux/ubuntu bionic InRelease [64.4 kB]                                                                   
Hit:35 http://ppa.launchpad.net/alexlarsson/flatpak/ubuntu bionic InRelease                                                                  
Hit:36 http://ppa.launchpad.net/apandada1/brightness-controller/ubuntu bionic InRelease                                                      
Hit:37 http://ppa.launchpad.net/cybermax-dexter/sdl2-backport/ubuntu bionic InRelease                                                        
Hit:38 http://ppa.launchpad.net/kxstudio-debian/libs/ubuntu bionic InRelease                                                                 
Hit:33 https://packagecloud.io/slacktechnologies/slack/debian jessie InRelease                                                               
Hit:39 http://ppa.launchpad.net/kxstudio-debian/music/ubuntu bionic InRelease                                                                
Hit:40 http://ppa.launchpad.net/kxstudio-debian/plugins/ubuntu bionic InRelease                                                              
Hit:41 http://ppa.launchpad.net/kxstudio-debian/apps/ubuntu bionic InRelease                                                                 
Hit:42 http://ppa.launchpad.net/kxstudio-debian/kxstudio/ubuntu bionic InRelease                                                             
Hit:43 http://ppa.launchpad.net/mixxx/mixxx/ubuntu bionic InRelease                                                                          
Hit:44 http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu bionic InRelease                                                         
Hit:45 http://packages.ros.org/ros/ubuntu bionic InRelease                                                                                   
Reading package lists... Done                                                                                                                
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: https://qgis.org/ubuntugis bionic InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY F7E06F06199EF2F2
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: https://qgis.org/ubuntu bionic InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY F7E06F06199EF2F2
W: GPG error: https://deb.torproject.org/torproject.org bionic InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 74A941BA219EC810
E: The repository 'https://deb.torproject.org/torproject.org bionic InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ 
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ code .
(base) dhankar@dhankar-1:~/temp/flask/learn-flask
```
#
- content of the file = /etc/apt/sources.list.d/mongodb-org-4.4.list
> deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse
#
```
sudo apt-get install -y mongodb-org
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ sudo apt-get install -y mongodb-org
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package mongodb-org

```

#
```
#@#
(base) dhankar@dhankar-1:/usr/bin$ mongo --version
MongoDB shell version v3.6.3
git version: 9586e557d54ef70f9ca4b43c26892cd55257e1a5
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distarch: x86_64
    target_arch: x86_64

(base) dhankar@dhankar-1:/usr/bin$ mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
	http://docs.mongodb.org/
Questions? Try the support group
	http://groups.google.com/group/mongodb-user
Server has startup warnings: 
2020-09-24T09:23:10.707+0530 I STORAGE  [initandlisten] 
2020-09-24T09:23:10.707+0530 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2020-09-24T09:23:10.707+0530 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2020-09-24T09:23:12.853+0530 I CONTROL  [initandlisten] 
2020-09-24T09:23:12.853+0530 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2020-09-24T09:23:12.853+0530 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2020-09-24T09:23:12.853+0530 I CONTROL  [initandlisten] 
> 
> 

```
#
- MongoDB connect with a connection string using - tls or ssl 
#
```
# Source - official Mongo 
#
You can run mongo shell with a connection string that specifies the host and port and other connection options. For example, the following includes the tls:

mongo "mongodb://mongodb0.example.com:27017/testdb?tls=true"

The tls option is available starting in MongoDB 4.2. In earlier version, use the ssl option.

To connect mongo shell to a replica set, you can specify in the connection string the replica set members and name:
```
#
- Mongo Connection String Formats- https://docs.mongodb.com/manual/reference/connection-string/#connection-string-uri-format
#
```

```
#


- Install REDIS 
- Source - https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04

```

(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ sudo systemctl restart redis.service
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ sudo systemctl status redis
● redis-server.service - Advanced key-value store
   Loaded: loaded (/lib/systemd/system/redis-server.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2020-09-24 23:09:39 IST; 16s ago
     Docs: http://redis.io/documentation,
           man:redis-server(1)
  Process: 29162 ExecStop=/bin/kill -s TERM $MAINPID (code=exited, status=0/SUCCESS)
  Process: 29165 ExecStart=/usr/bin/redis-server /etc/redis/redis.conf (code=exited, status=0/SUCCESS)
 Main PID: 29178 (redis-server)
    Tasks: 4 (limit: 4915)
   CGroup: /system.slice/redis-server.service
           └─29178 /usr/bin/redis-server 127.0.0.1:6379

Sep 24 23:09:39 dhankar-1 systemd[1]: Starting Advanced key-value store...
Sep 24 23:09:39 dhankar-1 systemd[1]: redis-server.service: Can't open PID file /var/run/redis/redis-server.pid (yet?) after start: No such fi
Sep 24 23:09:39 dhankar-1 systemd[1]: Started Advanced key-value store.

```
#
- redis-cli 

```
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ redis-cli
127.0.0.1:6379> 
127.0.0.1:6379> ping
PONG
127.0.0.1:6379> 
127.0.0.1:6379> set test "It's working!"
OK
127.0.0.1:6379> set test "It's work!"
OK
127.0.0.1:6379> get test
"It's work!"
127.0.0.1:6379> 

```
> As a final test, we will check whether Redis is able to persist data even after it’s been stopped or restarted. To do this, first restart the Redis instance:
```
    sudo systemctl restart redis
    "It's work!"
127.0.0.1:6379> exit
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ 
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ sudo systemctl restart redis
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ 
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ redis-cli
127.0.0.1:6379> 
127.0.0.1:6379> get test
"It's work!"
127.0.0.1:6379> 
127.0.0.1:6379> 

```
#
- Binding to localhost - By default, Redis is only accessible from localhost.

```
################################## NETWORK #####################################

# By default, if no "bind" configuration directive is specified, Redis listens
# for connections from all the network interfaces available on the server.
# It is possible to listen to just one or multiple selected interfaces using
# the "bind" configuration directive, followed by one or more IP addresses.
#
# Examples:
#
# bind 192.168.1.100 10.0.0.1
# bind 127.0.0.1 ::1
#
# ~~~ WARNING ~~~ If the computer running Redis is directly exposed to the
# internet, binding to all the interfaces is dangerous and will expose the
# instance to everybody on the internet. So by default we uncomment the
# following bind directive, that will force Redis to listen only into
# the IPv4 lookback interface address (this means Redis will be able to
# accept connections only from clients running into the same computer it
# is running).
#
# IF YOU ARE SURE YOU WANT YOUR INSTANCE TO LISTEN TO ALL THE INTERFACES
# JUST COMMENT THE FOLLOWING LINE.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#@#

bind 127.0.0.1 ::1

# Protected mode is a layer of security protection, in order to avoid that
# Redis instances left open on the internet are accessed and exploited.
#
# When protected mode is on and if:
#
# 1) The server is not binding explicitly to a set of addresses using the
#    "bind" directive.
# 2) No password is configured.
#
# The server only accepts connections from clients connecting from the
# IPv4 and IPv6 loopback addresses 127.0.0.1 and ::1, and from Unix domain
# sockets.
#
# By default protected mode is enabled. You should disable it only if
# you are sure you want clients from other hosts to connect to Redis
# even if no authentication is configured, nor a specific set of interfaces
# are explicitly listed using the "bind" directive.
protected-mode yes

# Accept connections on the specified port, default is 6379 (IANA #815344).
# If port 0 is specified Redis will not listen on a TCP socket.
port 6379

# TCP listen() backlog.
#
# In high requests-per-second environments you need an high backlog in order
# to avoid slow clients connections issues. Note that the Linux kernel
# will silently truncate it to the value of /proc/sys/net/core/somaxconn so
# make sure to raise both the value of somaxconn and tcp_max_syn_backlog
# in order to get the desired effect.
tcp-backlog 511

# Unix socket.
#
# Specify the path for the Unix socket that will be used to listen for
# incoming connections. There is no default, so Redis will not listen
# on a unix socket when not specified.
#
# unixsocket /var/run/redis/redis-server.sock
# unixsocketperm 700

# Close the connection after a client is idle for N seconds (0 to disable)
timeout 0

# TCP keepalive.
#
# If non-zero, use SO_KEEPALIVE to send TCP ACKs to clients in absence
# of communication. This is useful for two reasons:
#
# 1) Detect dead peers.
# 2) Take the connection alive from the point of view of network
#    equipment in the middle.
#
# On Linux, the specified value (in seconds) is the period used to send ACKs.
# Note that to close the connection the double of the time is needed.
# On other kernels the period depends on the kernel configuration.
#
# A reasonable value for this option is 300 seconds, which is the new
# Redis default starting with Redis 3.2.1.
tcp-keepalive 300
```
#
```
```
#

#
```
```
#


#
```
```
#


#
```
```
#