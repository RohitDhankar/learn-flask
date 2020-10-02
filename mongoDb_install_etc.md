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
$ sudo apt-get install -y mongodb-org
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
- On Own Local Ubuntu 18 - Mongo Updated to latest version . 
- Official MongoDB install - sudo apt-get install -y mongodb-org
- Source - https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

#
```

$ wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
OK
$ sudo apt-get install gnupg
Reading package lists... Done
Building dependency tree       
Reading state information... Done
gnupg is already the newest version (2.2.4-1ubuntu1.3).
The following packages were automatically installed and are no longer required:
  libgoogle-perftools4 libtcmalloc-minimal4 libyaml-cpp0.5v5 linux-hwe-5.4-headers-5.4.0-45 mongo-tools mongodb-server-core
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
OK
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse
$ sudo apt-get update
.........
$ sudo apt-get install -y mongodb-org
Reading package lists... Done
Building dependency tree       
Reading state information... Done
mongodb-org is already the newest version (4.4.1).
The following packages were automatically installed and are no longer required:
  libgoogle-perftools4 libtcmalloc-minimal4 libyaml-cpp0.5v5 linux-hwe-5.4-headers-5.4.0-45 mongo-tools mongodb-server-core
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.
#
#

$ sudo apt autoremove
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be REMOVED:
  libgoogle-perftools4 libtcmalloc-minimal4 libyaml-cpp0.5v5 linux-hwe-5.4-headers-5.4.0-45 mongo-tools mongodb-server-core
0 upgraded, 0 newly installed, 6 to remove and 31 not upgraded.
After this operation, 215 MB disk space will be freed.
Do you want to continue? [Y/n] y
(Reading database ... 350291 files and directories currently installed.)
Removing mongodb-server-core (1:3.6.3-0ubuntu1.1) ...
Removing libgoogle-perftools4 (2.5-2.2ubuntu3) ...
Removing libtcmalloc-minimal4 (2.5-2.2ubuntu3) ...
Removing libyaml-cpp0.5v5:amd64 (0.5.2-4ubuntu1) ...
Removing linux-hwe-5.4-headers-5.4.0-45 (5.4.0-45.49~18.04.2) ...
Removing mongo-tools (3.6.3-0ubuntu1) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for libc-bin (2.27-3ubuntu1.2) ...
$ 
$ echo "mongodb-org hold" | sudo dpkg --set-selections
$ echo "mongodb-org-server hold" | sudo dpkg --set-selections
$ echo "mongodb-org-shell hold" | sudo dpkg --set-selections
$ echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
$ echo "mongodb-org-tools hold" | sudo dpkg --set-selections
$ echo "mongodb-org-tools hold" | sudo dpkg --set-selections
$ cd /var/lib/mongodb
(base) dhankar@dhankar-1:/var/lib/mongodb$ ls -ltr
total 272
-rw------- 1 mongodb mongodb    21 Oct  1 22:09 WiredTiger.lock
-rw------- 1 mongodb mongodb    47 Oct  1 22:09 WiredTiger
-rw------- 1 mongodb mongodb   114 Oct  1 22:09 storage.bson
-rw------- 1 mongodb mongodb  4096 Oct  1 22:10 index-5-465390074794491220.wt
-rw------- 1 mongodb mongodb  4096 Oct  1 22:10 collection-4-465390074794491220.wt
-rw------- 1 mongodb mongodb  4096 Oct  1 22:10 WiredTigerHS.wt
-rw------- 1 mongodb mongodb 20480 Oct  1 22:10 _mdb_catalog.wt
-rw------- 1 mongodb mongodb     6 Oct  1 22:10 mongod.lock
-rw------- 1 mongodb mongodb 20480 Oct  1 22:10 index-1-465390074794491220.wt
-rw------- 1 mongodb mongodb 20480 Oct  1 22:10 collection-0-465390074794491220.wt
drwx------ 2 mongodb mongodb  4096 Oct  1 22:10 journal
-rw------- 1 mongodb mongodb 36864 Oct  1 22:11 index-3-465390074794491220.wt
-rw------- 1 mongodb mongodb 36864 Oct  1 22:11 collection-2-465390074794491220.wt
-rw------- 1 mongodb mongodb  4096 Oct  1 22:11 index-6-465390074794491220.wt
-rw------- 1 mongodb mongodb 36864 Oct  1 22:12 sizeStorer.wt
-rw------- 1 mongodb mongodb 61440 Oct  1 22:30 WiredTiger.wt
-rw------- 1 mongodb mongodb  1254 Oct  1 22:30 WiredTiger.turtle
drwx------ 2 mongodb mongodb  4096 Oct  1 22:30 diagnostic.data
(base) dhankar@dhankar-1:/var/lib/mongodb$ 

#
(base) dhankar@dhankar-1:/var/lib/mongodb$ ps --no-headers -o comm 1
systemd
(base) dhankar@dhankar-1:/var/lib/mongodb$ sudo systemctl start mongod
(base) dhankar@dhankar-1:/var/lib/mongodb$ sudo systemctl status mongod
● mongod.service - MongoDB Database Server
   Loaded: loaded (/lib/systemd/system/mongod.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2020-10-01 22:10:36 IST; 24min ago
     Docs: https://docs.mongodb.org/manual
 Main PID: 22920 (mongod)
   CGroup: /system.slice/mongod.service
           └─22920 /usr/bin/mongod --config /etc/mongod.conf

Oct 01 22:10:36 dhankar-1 systemd[1]: Started MongoDB Database Server.
(base) dhankar@dhankar-1:/var/lib/mongodb$ 

#

#### FOOBAR-- below the mongo - shell which is from Official Installs of the MongoDB-Org -- sudo apt-get install -y mongodb-org
## -SOURCE- https://docs.mongodb.com/manual/mongo/
#

(base) dhankar@dhankar-1:/var/lib/mongodb$ sudo systemctl enable mongod
(base) dhankar@dhankar-1:/var/lib/mongodb$ mongo
MongoDB shell version v4.4.1
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("0cb6e1fd-5f8b-4b19-b1f8-4c52927cf410") }
MongoDB server version: 4.4.1
---
The server generated these startup warnings when booting: 
        2020-10-01T22:10:36.876+05:30: ***** SERVER RESTARTED *****
        2020-10-01T22:10:36.882+05:30: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
        2020-10-01T22:10:37.911+05:30: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
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
> 

#

######## FOOBAR-- below the mongo - shell which is from within default Ubuntu Repositories ? 
#

(base) dhankar@dhankar-1:/usr/bin$ mongo
MongoDB shell version v4.4.1
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("63602b81-52cf-4619-93c6-0d52d740647d") }
MongoDB server version: 4.4.1
---
The server generated these startup warnings when booting: 
        2020-10-02T12:45:25.670+05:30: ***** SERVER RESTARTED *****
        2020-10-02T12:45:35.034+05:30: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
        2020-10-02T12:45:40.812+05:30: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
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
> 

```
#

#
```
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> 
> use flask_test
switched to db flask_test
> 
> db.coll_1.insert({name: "Rohit Dhankar", alias: 'rd'})
WriteResult({ "nInserted" : 1 })
> 
> db
flask_test
> 

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