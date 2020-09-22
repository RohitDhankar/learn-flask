> Start Flask 

#@#

> running gunicorn in front of Flask

```
(drf_venv) dhankar@dhankar-1:~/temp/flask/learn-flask$ gunicorn server1:app_fServer
[2020-09-21 18:53:44 +0530] [26837] [INFO] Starting gunicorn 20.0.4
[2020-09-21 18:53:44 +0530] [26837] [INFO] Listening at: http://127.0.0.1:8000 (26837)
[2020-09-21 18:53:44 +0530] [26837] [INFO] Using worker: sync
[2020-09-21 18:53:44 +0530] [26839] [INFO] Booting worker with pid: 26839
<flask_mysqldb.MySQL object at 0x7f76d30f40a0>
[2020-09-21 18:53:48 +0530] [26837] [INFO] Handling signal: winch

```
#
- running - uvicorn in front of FastAPI

# 

```
(drf_venv) dhankar@dhankar-1:~/temp/flask/learn-flask$ uvicorn server2:fastApp
INFO:     Started server process [28089]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

```

> app_test.py

```
(drf_venv) dhankar@dhankar-1:~/temp/flask/learn-flask$ ls -ltr
total 28
-rw-r--r-- 1 dhankar dhankar   47 Sep 19 13:29 README.md
-rw-r--r-- 1 dhankar dhankar 2449 Sep 19 14:02 OwnCodeLogs_.md
drwxr-xr-x 2 dhankar dhankar 4096 Sep 19 14:05 static
-rw-r--r-- 1 dhankar dhankar  192 Sep 19 14:08 app.py
drwxr-xr-x 2 dhankar dhankar 4096 Sep 19 15:07 templates
-rw-r--r-- 1 dhankar dhankar  364 Sep 19 15:28 app_test.py
drwxr-xr-x 2 dhankar dhankar 4096 Sep 19 15:29 __pycache__
(drf_venv) dhankar@dhankar-1:~/temp/flask/learn-flask$ 
(drf_venv) dhankar@dhankar-1:~/temp/flask/learn-flask$ tree
.
├── app.py
├── app_test.py
├── OwnCodeLogs_.md
├── __pycache__
│   └── app.cpython-38.pyc
├── README.md
├── static
└── templates
    ├── base.html
    └── index.html

3 directories, 7 files
(drf_venv) dhankar@dhankar-1:~/temp/flask/learn-flask$ 
(drf_venv) dhankar@dhankar-1:~/temp/flask/learn-flask$ python app_test.py
F
======================================================================
FAIL: test_index (__main__.BasicTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "app_test.py", line 12, in test_index
    self.assertEqual(response.data, b'Hello, World!')
AssertionError: b'<p> random HTML </p>' != b'Hello, World!'

----------------------------------------------------------------------
Ran 1 test in 0.004s

FAILED (failures=1)
(drf_venv) dhankar@dhankar-1:~/temp/flask/learn-flask$ 
```

```
(drf_venv) dhankar@dhankar-1:~/temp/flask/learn-flask$ python app.py
<built-in function globals>
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 126-129-393
```

```
(drf_venv) dhankar@dhankar-1:~/temp/flask$ pip install flask flask-sqlalchemy
Collecting flask
  Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
     |████████████████████████████████| 94 kB 377 kB/s 
Collecting flask-sqlalchemy
  Downloading Flask_SQLAlchemy-2.4.4-py2.py3-none-any.whl (17 kB)
Collecting click>=5.1
  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
     |████████████████████████████████| 82 kB 148 kB/s 
Collecting itsdangerous>=0.24
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Werkzeug>=0.15
  Using cached Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
Requirement already satisfied: Jinja2>=2.10.1 in /home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages (from flask) (2.11.2)
Collecting SQLAlchemy>=0.8.0
  Downloading SQLAlchemy-1.3.19-cp38-cp38-manylinux2010_x86_64.whl (1.3 MB)
     |████████████████████████████████| 1.3 MB 52.2 MB/s 
Requirement already satisfied: MarkupSafe>=0.23 in /home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages (from Jinja2>=2.10.1->flask) (1.1.1)
Installing collected packages: click, itsdangerous, Werkzeug, flask, SQLAlchemy, flask-sqlalchemy
Successfully installed SQLAlchemy-1.3.19 Werkzeug-1.0.1 click-7.1.2 flask-1.1.2 flask-sqlalchemy-2.4.4 itsdangerous-1.1.0
(drf_venv) dhankar@dhankar-1:~/temp/flask$ 
```

#
- print(globals())

```
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f26f3778be0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/dhankar/temp/flask/learn-flask/app.py', '__cached__': None, 'Flask': <class 'flask.app.Flask'>, 'app': <Flask 'app'>, 'index': <function index at 0x7f26f36964c0>}
```

#
> Jinja Template Tags - diff from Django template tags - 
```
 <!-- This is Django Style - below is Flask/Jinja Style <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet"> -->
```

#

- flask_sqlalchemy - SQLALCHEMY_TRACK_MODIFICATIONS - Deprecation Warning

```
(drf_venv) dhankar@dhankar-1:~/temp/flask/learn-flask$ python
Python 3.8.5 (default, Aug  5 2020, 08:36:46) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import db
/home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages/flask_sqlalchemy/__init__.py:833: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
>>> 
```

#

```
#@# 
(drf_venv) dhankar@dhankar-1:~/temp/flask/learn-flask$ pip install flask-mysqldb
Collecting flask-mysqldb
  Using cached Flask-MySQLdb-0.2.0.tar.gz (2.1 kB)
Requirement already satisfied: Flask>=0.10 in /home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages (from flask-mysqldb) (1.1.2)
Collecting mysqlclient
  Using cached mysqlclient-2.0.1.tar.gz (87 kB)
    ERROR: Command errored out with exit status 1:
     command: /home/dhankar/anaconda3/envs/drf_venv/bin/python -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-uv2nktre/mysqlclient/setup.py'"'"'; __file__='"'"'/tmp/pip-install-uv2nktre/mysqlclient/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /tmp/pip-pip-egg-info-w7d5n4gb
         cwd: /tmp/pip-install-uv2nktre/mysqlclient/
    Complete output (12 lines):
    /bin/sh: 1: mysql_config: not found
    /bin/sh: 1: mariadb_config: not found
    /bin/sh: 1: mysql_config: not found
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-install-uv2nktre/mysqlclient/setup.py", line 15, in <module>
        metadata, options = get_config()
      File "/tmp/pip-install-uv2nktre/mysqlclient/setup_posix.py", line 65, in get_config
        libs = mysql_config("libs")
      File "/tmp/pip-install-uv2nktre/mysqlclient/setup_posix.py", line 31, in mysql_config
        raise OSError("{} not found".format(_mysql_config_path))
    OSError: mysql_config not found
    ----------------------------------------
ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
(drf_venv) dhankar@dhankar-1:~/temp/flask/learn-flask$ 
(drf_venv) dhankar@dhankar-1:~/temp/flask/learn-flask$ 

#@#

(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ sudo apt install libmysqlclient-dev
[sudo] password for dhankar: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  libmysqlclient-dev
0 upgraded, 1 newly installed, 0 to remove and 72 not upgraded.
Need to get 992 kB of archives.
After this operation, 6,013 kB of additional disk space will be used.
Get:1 http://in.archive.ubuntu.com/ubuntu bionic-updates/main amd64 libmysqlclient-dev amd64 5.7.31-0ubuntu0.18.04.1 [992 kB]
Fetched 992 kB in 5s (186 kB/s)            
Selecting previously unselected package libmysqlclient-dev.
(Reading database ... 332012 files and directories currently installed.)
Preparing to unpack .../libmysqlclient-dev_5.7.31-0ubuntu0.18.04.1_amd64.deb ...
Unpacking libmysqlclient-dev (5.7.31-0ubuntu0.18.04.1) ...
Setting up libmysqlclient-dev (5.7.31-0ubuntu0.18.04.1) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ 

```
- AWS CLI 

```
aws ec2 describe-instance-attribute --instance-id i-0179ecbd02281a80d --attribute groupSet
(base) dhankar@dhankar-1:~/temp/flask/learn-flask$ aws ec2 describe-instance-attribute --instance-id i-0179ecbd02281a80d --attribute groupSet

An error occurred (InvalidInstanceID.NotFound) when calling the DescribeInstanceAttribute operation: The instance ID 'i-0179ecbd02281a80d' does not exist

```
#

- Public IPv4 DNS == ec2-13-235-81-66.ap-south-1.compute.amazonaws.com
```
(base) dhankar@dhankar-1:~/temp/flask/learn-flask/aws_instance$ ssh -i "strato.pem" ubuntu@ec2-13-235-81-66.ap-south-1.compute.amazonaws.com
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.3.0-1035-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Sep 22 14:40:10 UTC 2020

  System load:  0.0               Processes:           90
  Usage of /:   14.4% of 7.69GB   Users logged in:     0
  Memory usage: 17%               IP address for eth0: 172.31.13.163
  Swap usage:   0%

0 packages can be updated.
0 updates are security updates.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ip-172-31-13-163:~$ 
ubuntu@ip-172-31-13-163:~$ 

```
#
- Upgrade Ubuntu box on first login 

```
sudo apt-get update && sudo apt-get upgrade -y

ubuntu@ip-172-31-13-163:~$ 
ubuntu@ip-172-31-13-163:~$ sudo apt-get update && sudo apt-get upgrade -y
Get:1 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic InRelease [242 kB]
Get:2 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]
Get:3 http://security.ubuntu.com/ubuntu bionic-security/main amd64 Packages [860 kB]
Get:4 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]
Get:5 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]
Get:6 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic/universe amd64 Packages [8570 kB]  
Get:7 http://security.ubuntu.com/ubuntu bionic-security/main Translation-en [267 kB]                     
Get:8 http://security.ubuntu.com/ubuntu bionic-security/restricted amd64 Packages [90.9 kB]                              
Get:9 http://security.ubuntu.com/ubuntu bionic-security/restricted Translation-en [19.4 kB]                              
Get:10 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 Packages [706 kB]        
Get:11 http://security.ubuntu.com/ubuntu bionic-security/universe Translation-en [235 kB]        
Get:12 http://security.ubuntu.com/ubuntu bionic-security/multiverse amd64 Packages [8512 B] 
Get:13 http://security.ubuntu.com/ubuntu bionic-security/multiverse Translation-en [2908 B]
Get:14 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic/universe Translation-en [4941 kB]                                              
Get:15 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic/multiverse amd64 Packages [151 kB]                                             
Get:16 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic/multiverse Translation-en [108 kB]                                             
Get:17 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages [1087 kB]                                          
Get:18 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main Translation-en [360 kB]                                           
Get:19 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/restricted amd64 Packages [107 kB]                                     
Get:20 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/restricted Translation-en [23.0 kB]                                    
Get:21 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 Packages [1114 kB]                                      
Get:22 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/universe Translation-en [348 kB]                                       
Get:23 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/multiverse amd64 Packages [21.8 kB]                                    
Get:24 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/multiverse Translation-en [6920 B]                                     
Get:25 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-backports/main amd64 Packages [7516 B]                                         
Get:26 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-backports/main Translation-en [4764 B]                                         
Get:27 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-backports/universe amd64 Packages [7736 B]                                     
Get:28 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-backports/universe Translation-en [4588 B]                                     
Fetched 19.5 MB in 39s (505 kB/s)                                                                                                            
Reading package lists... Done
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Calculating upgrade... Done
The following packages have been kept back:
  linux-aws linux-headers-aws linux-image-aws
The following packages will be upgraded:
  bsdutils busybox-initramfs busybox-static cloud-init dirmngr fdisk gnupg gnupg-l10n gnupg-utils gpg gpg-agent gpg-wks-client
  gpg-wks-server gpgconf gpgsm gpgv initramfs-tools initramfs-tools-bin initramfs-tools-core libblkid1 libfdisk1 libmount1 libsmartcols1
  libssl1.0.0 libuuid1 mount util-linux uuid-runtime
28 upgraded, 0 newly installed, 0 to remove and 3 not upgraded.
Need to get 6565 kB of archives.
After this operation, 91.1 kB of additional disk space will be used.
Get:1 http://security.ubuntu.com/ubuntu bionic-security/main amd64 busybox-initramfs amd64 1:1.27.2-2ubuntu3.3 [165 kB]
Get:2 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 bsdutils amd64 1:2.31.1-0.4ubuntu3.7 [60.2 kB]
Get:3 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 libuuid1 amd64 2.31.1-0.4ubuntu3.7 [20.1 kB]
Get:4 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 libblkid1 amd64 2.31.1-0.4ubuntu3.7 [124 kB]
Get:5 http://security.ubuntu.com/ubuntu bionic-security/main amd64 busybox-static amd64 1:1.27.2-2ubuntu3.3 [918 kB]
Get:6 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 libfdisk1 amd64 2.31.1-0.4ubuntu3.7 [164 kB]
Get:7 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 libmount1 amd64 2.31.1-0.4ubuntu3.7 [136 kB]
Get:8 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 libsmartcols1 amd64 2.31.1-0.4ubuntu3.7 [83.8 kB]
Get:9 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 fdisk amd64 2.31.1-0.4ubuntu3.7 [108 kB]
Get:10 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 util-linux amd64 2.31.1-0.4ubuntu3.7 [904 kB]
Get:11 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 mount amd64 2.31.1-0.4ubuntu3.7 [107 kB]
Get:12 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 uuid-runtime amd64 2.31.1-0.4ubuntu3.7 [34.8 kB]
Get:13 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 gpg-wks-client amd64 2.2.4-1ubuntu1.3 [91.8 kB]
Get:14 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 dirmngr amd64 2.2.4-1ubuntu1.3 [316 kB]
Get:15 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 gpg amd64 2.2.4-1ubuntu1.3 [467 kB]
Get:16 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 gnupg-utils amd64 2.2.4-1ubuntu1.3 [127 kB]                 
Get:17 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 gnupg-l10n all 2.2.4-1ubuntu1.3 [49.7 kB]                   
Get:18 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 gpg-agent amd64 2.2.4-1ubuntu1.3 [227 kB]                   
Get:19 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 gpgsm amd64 2.2.4-1ubuntu1.3 [215 kB]                       
Get:20 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 gpgconf amd64 2.2.4-1ubuntu1.3 [123 kB]                     
Get:21 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 gnupg amd64 2.2.4-1ubuntu1.3 [249 kB]                       
Get:22 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 gpg-wks-server amd64 2.2.4-1ubuntu1.3 [85.0 kB]             
Get:23 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 gpgv amd64 2.2.4-1ubuntu1.3 [198 kB]                        
Get:24 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 initramfs-tools-core all 0.130ubuntu3.10 [48.3 kB]          
Get:25 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 initramfs-tools all 0.130ubuntu3.10 [9588 B]                
Get:26 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 initramfs-tools-bin amd64 0.130ubuntu3.10 [10.3 kB]         
Get:27 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 libssl1.0.0 amd64 1.0.2n-1ubuntu5.4 [1088 kB]               
Get:28 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 cloud-init all 20.3-2-g371b392c-0ubuntu1~18.04.1 [434 kB]   
Fetched 6565 kB in 14s (482 kB/s)                                                                                                            
Preconfiguring packages ...
(Reading database ... 57083 files and directories currently installed.)
Preparing to unpack .../bsdutils_1%3a2.31.1-0.4ubuntu3.7_amd64.deb ...
Unpacking bsdutils (1:2.31.1-0.4ubuntu3.7) over (1:2.31.1-0.4ubuntu3.6) ...
Setting up bsdutils (1:2.31.1-0.4ubuntu3.7) ...
(Reading database ... 57083 files and directories currently installed.)
Preparing to unpack .../libuuid1_2.31.1-0.4ubuntu3.7_amd64.deb ...
Unpacking libuuid1:amd64 (2.31.1-0.4ubuntu3.7) over (2.31.1-0.4ubuntu3.6) ...
Setting up libuuid1:amd64 (2.31.1-0.4ubuntu3.7) ...
(Reading database ... 57083 files and directories currently installed.)
Preparing to unpack .../libblkid1_2.31.1-0.4ubuntu3.7_amd64.deb ...
Unpacking libblkid1:amd64 (2.31.1-0.4ubuntu3.7) over (2.31.1-0.4ubuntu3.6) ...
Setting up libblkid1:amd64 (2.31.1-0.4ubuntu3.7) ...
(Reading database ... 57083 files and directories currently installed.)
Preparing to unpack .../libfdisk1_2.31.1-0.4ubuntu3.7_amd64.deb ...
Unpacking libfdisk1:amd64 (2.31.1-0.4ubuntu3.7) over (2.31.1-0.4ubuntu3.6) ...
Setting up libfdisk1:amd64 (2.31.1-0.4ubuntu3.7) ...
(Reading database ... 57083 files and directories currently installed.)
Preparing to unpack .../libmount1_2.31.1-0.4ubuntu3.7_amd64.deb ...
Unpacking libmount1:amd64 (2.31.1-0.4ubuntu3.7) over (2.31.1-0.4ubuntu3.6) ...
Setting up libmount1:amd64 (2.31.1-0.4ubuntu3.7) ...
(Reading database ... 57083 files and directories currently installed.)
Preparing to unpack .../libsmartcols1_2.31.1-0.4ubuntu3.7_amd64.deb ...
Unpacking libsmartcols1:amd64 (2.31.1-0.4ubuntu3.7) over (2.31.1-0.4ubuntu3.6) ...
Setting up libsmartcols1:amd64 (2.31.1-0.4ubuntu3.7) ...
(Reading database ... 57083 files and directories currently installed.)
Preparing to unpack .../fdisk_2.31.1-0.4ubuntu3.7_amd64.deb ...
Unpacking fdisk (2.31.1-0.4ubuntu3.7) over (2.31.1-0.4ubuntu3.6) ...
Setting up fdisk (2.31.1-0.4ubuntu3.7) ...
(Reading database ... 57083 files and directories currently installed.)
Preparing to unpack .../util-linux_2.31.1-0.4ubuntu3.7_amd64.deb ...
Unpacking util-linux (2.31.1-0.4ubuntu3.7) over (2.31.1-0.4ubuntu3.6) ...
Setting up util-linux (2.31.1-0.4ubuntu3.7) ...
(Reading database ... 57083 files and directories currently installed.)
Preparing to unpack .../00-mount_2.31.1-0.4ubuntu3.7_amd64.deb ...
Unpacking mount (2.31.1-0.4ubuntu3.7) over (2.31.1-0.4ubuntu3.6) ...
Preparing to unpack .../01-uuid-runtime_2.31.1-0.4ubuntu3.7_amd64.deb ...
Unpacking uuid-runtime (2.31.1-0.4ubuntu3.7) over (2.31.1-0.4ubuntu3.6) ...
Preparing to unpack .../02-gpg-wks-client_2.2.4-1ubuntu1.3_amd64.deb ...
Unpacking gpg-wks-client (2.2.4-1ubuntu1.3) over (2.2.4-1ubuntu1.2) ...
Preparing to unpack .../03-dirmngr_2.2.4-1ubuntu1.3_amd64.deb ...
Unpacking dirmngr (2.2.4-1ubuntu1.3) over (2.2.4-1ubuntu1.2) ...
Preparing to unpack .../04-gpg_2.2.4-1ubuntu1.3_amd64.deb ...
Unpacking gpg (2.2.4-1ubuntu1.3) over (2.2.4-1ubuntu1.2) ...
Preparing to unpack .../05-gnupg-utils_2.2.4-1ubuntu1.3_amd64.deb ...
Unpacking gnupg-utils (2.2.4-1ubuntu1.3) over (2.2.4-1ubuntu1.2) ...
Preparing to unpack .../06-gnupg-l10n_2.2.4-1ubuntu1.3_all.deb ...
Unpacking gnupg-l10n (2.2.4-1ubuntu1.3) over (2.2.4-1ubuntu1.2) ...
Preparing to unpack .../07-gpg-agent_2.2.4-1ubuntu1.3_amd64.deb ...
Unpacking gpg-agent (2.2.4-1ubuntu1.3) over (2.2.4-1ubuntu1.2) ...
Preparing to unpack .../08-gpgsm_2.2.4-1ubuntu1.3_amd64.deb ...
Unpacking gpgsm (2.2.4-1ubuntu1.3) over (2.2.4-1ubuntu1.2) ...
Preparing to unpack .../09-gpgconf_2.2.4-1ubuntu1.3_amd64.deb ...
Unpacking gpgconf (2.2.4-1ubuntu1.3) over (2.2.4-1ubuntu1.2) ...
Preparing to unpack .../10-gnupg_2.2.4-1ubuntu1.3_amd64.deb ...
Unpacking gnupg (2.2.4-1ubuntu1.3) over (2.2.4-1ubuntu1.2) ...
Preparing to unpack .../11-gpg-wks-server_2.2.4-1ubuntu1.3_amd64.deb ...
Unpacking gpg-wks-server (2.2.4-1ubuntu1.3) over (2.2.4-1ubuntu1.2) ...
Preparing to unpack .../12-gpgv_2.2.4-1ubuntu1.3_amd64.deb ...
Unpacking gpgv (2.2.4-1ubuntu1.3) over (2.2.4-1ubuntu1.2) ...
Setting up gpgv (2.2.4-1ubuntu1.3) ...
(Reading database ... 57083 files and directories currently installed.)
Preparing to unpack .../0-initramfs-tools-core_0.130ubuntu3.10_all.deb ...
Unpacking initramfs-tools-core (0.130ubuntu3.10) over (0.130ubuntu3.9) ...
Preparing to unpack .../1-initramfs-tools_0.130ubuntu3.10_all.deb ...
Unpacking initramfs-tools (0.130ubuntu3.10) over (0.130ubuntu3.9) ...
Preparing to unpack .../2-initramfs-tools-bin_0.130ubuntu3.10_amd64.deb ...
Unpacking initramfs-tools-bin (0.130ubuntu3.10) over (0.130ubuntu3.9) ...
Preparing to unpack .../3-busybox-initramfs_1%3a1.27.2-2ubuntu3.3_amd64.deb ...
Unpacking busybox-initramfs (1:1.27.2-2ubuntu3.3) over (1:1.27.2-2ubuntu3.2) ...
Preparing to unpack .../4-busybox-static_1%3a1.27.2-2ubuntu3.3_amd64.deb ...
Unpacking busybox-static (1:1.27.2-2ubuntu3.3) over (1:1.27.2-2ubuntu3.2) ...
Preparing to unpack .../5-libssl1.0.0_1.0.2n-1ubuntu5.4_amd64.deb ...
Unpacking libssl1.0.0:amd64 (1.0.2n-1ubuntu5.4) over (1.0.2n-1ubuntu5.3) ...
Preparing to unpack .../6-cloud-init_20.3-2-g371b392c-0ubuntu1~18.04.1_all.deb ...
Unpacking cloud-init (20.3-2-g371b392c-0ubuntu1~18.04.1) over (20.2-45-g5f7825e2-0ubuntu1~18.04.1) ...
Setting up libssl1.0.0:amd64 (1.0.2n-1ubuntu5.4) ...
Setting up gpgconf (2.2.4-1ubuntu1.3) ...
Setting up mount (2.31.1-0.4ubuntu3.7) ...
Setting up gpg-agent (2.2.4-1ubuntu1.3) ...
Setting up gnupg-l10n (2.2.4-1ubuntu1.3) ...
Setting up uuid-runtime (2.31.1-0.4ubuntu3.7) ...
Setting up busybox-initramfs (1:1.27.2-2ubuntu3.3) ...
Setting up gpgsm (2.2.4-1ubuntu1.3) ...
Setting up gnupg-utils (2.2.4-1ubuntu1.3) ...
Setting up busybox-static (1:1.27.2-2ubuntu3.3) ...
Setting up initramfs-tools-bin (0.130ubuntu3.10) ...
Setting up dirmngr (2.2.4-1ubuntu1.3) ...
Setting up gpg (2.2.4-1ubuntu1.3) ...
Setting up cloud-init (20.3-2-g371b392c-0ubuntu1~18.04.1) ...
Installing new version of config file /etc/cloud/cloud.cfg.d/05_logging.cfg ...
Installing new version of config file /etc/cloud/templates/hosts.freebsd.tmpl ...
Setting up initramfs-tools-core (0.130ubuntu3.10) ...
Setting up initramfs-tools (0.130ubuntu3.10) ...
update-initramfs: deferring update (trigger activated)
Setting up gpg-wks-server (2.2.4-1ubuntu1.3) ...
Setting up gpg-wks-client (2.2.4-1ubuntu1.3) ...
Setting up gnupg (2.2.4-1ubuntu1.3) ...
Processing triggers for systemd (237-3ubuntu10.42) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for rsyslog (8.32.0-1ubuntu4) ...
Processing triggers for mime-support (3.60ubuntu1) ...
Processing triggers for ureadahead (0.100.0-21) ...
Processing triggers for install-info (6.5.0.dfsg.1-2) ...
Processing triggers for libc-bin (2.27-3ubuntu1.2) ...
Processing triggers for initramfs-tools (0.130ubuntu3.10) ...
update-initramfs: Generating /boot/initrd.img-5.3.0-1035-aws
ubuntu@ip-172-31-13-163:~$ 
ubuntu@ip-172-31-13-163:~$ 


```

#
- install MongoDB

```

sudo apt-get install mongodb -y

ubuntu@ip-172-31-13-163:~$ 
ubuntu@ip-172-31-13-163:~$ sudo apt-get install mongodb -y
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libboost-filesystem1.65.1 libboost-iostreams1.65.1 libboost-program-options1.65.1 libboost-system1.65.1 libgoogle-perftools4 libpcrecpp0v5
  libsnappy1v5 libstemmer0d libtcmalloc-minimal4 libyaml-cpp0.5v5 mongo-tools mongodb-clients mongodb-server mongodb-server-core
The following NEW packages will be installed:
  libboost-filesystem1.65.1 libboost-iostreams1.65.1 libboost-program-options1.65.1 libboost-system1.65.1 libgoogle-perftools4 libpcrecpp0v5
  libsnappy1v5 libstemmer0d libtcmalloc-minimal4 libyaml-cpp0.5v5 mongo-tools mongodb mongodb-clients mongodb-server mongodb-server-core
0 upgraded, 15 newly installed, 0 to remove and 3 not upgraded.
Need to get 53.5 MB of archives.
After this operation, 217 MB of additional disk space will be used.
Get:1 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libboost-system1.65.1 amd64 1.65.1+dfsg-0ubuntu5 [10.5 kB]
Get:2 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libboost-filesystem1.65.1 amd64 1.65.1+dfsg-0ubuntu5 [40.3 kB]
Get:3 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libboost-iostreams1.65.1 amd64 1.65.1+dfsg-0ubuntu5 [29.2 kB]
Get:4 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libboost-program-options1.65.1 amd64 1.65.1+dfsg-0ubuntu5 [137 kB]
Get:5 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libtcmalloc-minimal4 amd64 2.5-2.2ubuntu3 [91.6 kB]
Get:6 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libgoogle-perftools4 amd64 2.5-2.2ubuntu3 [190 kB]
Get:7 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libpcrecpp0v5 amd64 2:8.39-9 [15.3 kB]
Get:8 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libstemmer0d amd64 0+svn585-1build1 [62.5 kB]
Get:9 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic/universe amd64 libyaml-cpp0.5v5 amd64 0.5.2-4ubuntu1 [150 kB]
Get:10 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic/universe amd64 mongo-tools amd64 3.6.3-0ubuntu1 [12.3 MB]
Get:11 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 libsnappy1v5 amd64 1.1.7-1 [16.0 kB]
Get:12 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 mongodb-clients amd64 1:3.6.3-0ubuntu1.1 [20.2 MB]
Get:13 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 mongodb-server-core amd64 1:3.6.3-0ubuntu1.1 [20.3 MB]  
Get:14 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 mongodb-server all 1:3.6.3-0ubuntu1.1 [12.6 kB]         
Get:15 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 mongodb amd64 1:3.6.3-0ubuntu1.1 [9968 B]               
Fetched 53.5 MB in 15s (3670 kB/s)                                                                                                           
Selecting previously unselected package libboost-system1.65.1:amd64.
(Reading database ... 57090 files and directories currently installed.)
Preparing to unpack .../00-libboost-system1.65.1_1.65.1+dfsg-0ubuntu5_amd64.deb ...
Unpacking libboost-system1.65.1:amd64 (1.65.1+dfsg-0ubuntu5) ...
Selecting previously unselected package libboost-filesystem1.65.1:amd64.
Preparing to unpack .../01-libboost-filesystem1.65.1_1.65.1+dfsg-0ubuntu5_amd64.deb ...
Unpacking libboost-filesystem1.65.1:amd64 (1.65.1+dfsg-0ubuntu5) ...
Selecting previously unselected package libboost-iostreams1.65.1:amd64.
Preparing to unpack .../02-libboost-iostreams1.65.1_1.65.1+dfsg-0ubuntu5_amd64.deb ...
Unpacking libboost-iostreams1.65.1:amd64 (1.65.1+dfsg-0ubuntu5) ...
Selecting previously unselected package libboost-program-options1.65.1:amd64.
Preparing to unpack .../03-libboost-program-options1.65.1_1.65.1+dfsg-0ubuntu5_amd64.deb ...
Unpacking libboost-program-options1.65.1:amd64 (1.65.1+dfsg-0ubuntu5) ...
Selecting previously unselected package libtcmalloc-minimal4.
Preparing to unpack .../04-libtcmalloc-minimal4_2.5-2.2ubuntu3_amd64.deb ...
Unpacking libtcmalloc-minimal4 (2.5-2.2ubuntu3) ...
Selecting previously unselected package libgoogle-perftools4.
Preparing to unpack .../05-libgoogle-perftools4_2.5-2.2ubuntu3_amd64.deb ...
Unpacking libgoogle-perftools4 (2.5-2.2ubuntu3) ...
Selecting previously unselected package libpcrecpp0v5:amd64.
Preparing to unpack .../06-libpcrecpp0v5_2%3a8.39-9_amd64.deb ...
Unpacking libpcrecpp0v5:amd64 (2:8.39-9) ...
Selecting previously unselected package libstemmer0d:amd64.
Preparing to unpack .../07-libstemmer0d_0+svn585-1build1_amd64.deb ...
Unpacking libstemmer0d:amd64 (0+svn585-1build1) ...
Selecting previously unselected package libyaml-cpp0.5v5:amd64.
Preparing to unpack .../08-libyaml-cpp0.5v5_0.5.2-4ubuntu1_amd64.deb ...
Unpacking libyaml-cpp0.5v5:amd64 (0.5.2-4ubuntu1) ...
Selecting previously unselected package mongo-tools.
Preparing to unpack .../09-mongo-tools_3.6.3-0ubuntu1_amd64.deb ...
Unpacking mongo-tools (3.6.3-0ubuntu1) ...
Selecting previously unselected package libsnappy1v5:amd64.
Preparing to unpack .../10-libsnappy1v5_1.1.7-1_amd64.deb ...
Unpacking libsnappy1v5:amd64 (1.1.7-1) ...
Selecting previously unselected package mongodb-clients.
Preparing to unpack .../11-mongodb-clients_1%3a3.6.3-0ubuntu1.1_amd64.deb ...
Unpacking mongodb-clients (1:3.6.3-0ubuntu1.1) ...
Selecting previously unselected package mongodb-server-core.
Preparing to unpack .../12-mongodb-server-core_1%3a3.6.3-0ubuntu1.1_amd64.deb ...
Unpacking mongodb-server-core (1:3.6.3-0ubuntu1.1) ...
Selecting previously unselected package mongodb-server.
Preparing to unpack .../13-mongodb-server_1%3a3.6.3-0ubuntu1.1_all.deb ...
Unpacking mongodb-server (1:3.6.3-0ubuntu1.1) ...
Selecting previously unselected package mongodb.
Preparing to unpack .../14-mongodb_1%3a3.6.3-0ubuntu1.1_amd64.deb ...
Unpacking mongodb (1:3.6.3-0ubuntu1.1) ...
Setting up libboost-iostreams1.65.1:amd64 (1.65.1+dfsg-0ubuntu5) ...
Setting up libstemmer0d:amd64 (0+svn585-1build1) ...
Setting up libboost-system1.65.1:amd64 (1.65.1+dfsg-0ubuntu5) ...
Setting up libtcmalloc-minimal4 (2.5-2.2ubuntu3) ...
Setting up libgoogle-perftools4 (2.5-2.2ubuntu3) ...
Setting up libsnappy1v5:amd64 (1.1.7-1) ...
Setting up libpcrecpp0v5:amd64 (2:8.39-9) ...
Setting up libyaml-cpp0.5v5:amd64 (0.5.2-4ubuntu1) ...
Setting up libboost-program-options1.65.1:amd64 (1.65.1+dfsg-0ubuntu5) ...
Setting up mongo-tools (3.6.3-0ubuntu1) ...
Setting up libboost-filesystem1.65.1:amd64 (1.65.1+dfsg-0ubuntu5) ...
Setting up mongodb-server-core (1:3.6.3-0ubuntu1.1) ...
Setting up mongodb-clients (1:3.6.3-0ubuntu1.1) ...
Setting up mongodb-server (1:3.6.3-0ubuntu1.1) ...
Created symlink /etc/systemd/system/multi-user.target.wants/mongodb.service → /lib/systemd/system/mongodb.service.
Setting up mongodb (1:3.6.3-0ubuntu1.1) ...
Processing triggers for systemd (237-3ubuntu10.42) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for ureadahead (0.100.0-21) ...
Processing triggers for libc-bin (2.27-3ubuntu1.2) ...
ubuntu@ip-172-31-13-163:~$ 

Processing triggers for libc-bin (2.27-3ubuntu1.2) ...
ubuntu@ip-172-31-13-163:~$ 
ubuntu@ip-172-31-13-163:~$ sudo apt-get update -y
Hit:1 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic InRelease
Hit:2 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-updates InRelease
Hit:3 http://security.ubuntu.com/ubuntu bionic-security InRelease        
Hit:4 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu bionic-backports InRelease
Reading package lists... Done                      
ubuntu@ip-172-31-13-163:~$ sudo service mongodb start
ubuntu@ip-172-31-13-163:~$ sudo service mongodb status
● mongodb.service - An object/document-oriented database
   Loaded: loaded (/lib/systemd/system/mongodb.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2020-09-22 14:50:24 UTC; 1min 14s ago
     Docs: man:mongod(1)
 Main PID: 18664 (mongod)
    Tasks: 23 (limit: 1140)
   CGroup: /system.slice/mongodb.service
           └─18664 /usr/bin/mongod --unixSocketPrefix=/run/mongodb --config /etc/mongodb.conf

Sep 22 14:50:24 ip-172-31-13-163 systemd[1]: Started An object/document-oriented database.
ubuntu@ip-172-31-13-163:~$ 


```
#

- MongoDB - CREATE == db.createUser

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
