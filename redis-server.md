```
(drf_venv) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ redis-server
15329:C 27 Sep 21:32:57.219 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
15329:C 27 Sep 21:32:57.220 # Redis version=4.0.9, bits=64, commit=00000000, modified=0, pid=15329, just started
15329:C 27 Sep 21:32:57.220 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
15329:M 27 Sep 21:32:57.220 # You requested maxclients of 10000 requiring at least 10032 max file descriptors.
15329:M 27 Sep 21:32:57.220 # Server can't set maximum open files to 10032 because of OS error: Operation not permitted.
15329:M 27 Sep 21:32:57.220 # Current maximum open files is 4096. maxclients has been reduced to 4064 to compensate for low ulimit. If you need higher maxclients increase 'ulimit -n'.
15329:M 27 Sep 21:32:57.220 # Creating Server TCP listening socket *:6379: bind: Address already in use
```
#

```
$ sudo service redis-server status
● redis-server.service - Advanced key-value store
   Loaded: loaded (/lib/systemd/system/redis-server.service; enabled; vendor preset: enabled)
   Active: active (running) since Sun 2020-09-27 21:37:32 IST; 1min 51s ago
     Docs: http://redis.io/documentation,
           man:redis-server(1)
  Process: 15799 ExecStart=/usr/bin/redis-server /etc/redis/redis.conf (code=exited, status=0/SUCCESS)
 Main PID: 15812 (redis-server)
    Tasks: 4 (limit: 4915)
   CGroup: /system.slice/redis-server.service
           └─15812 /usr/bin/redis-server 127.0.0.1:6379

Sep 27 21:37:32 dhankar-1 systemd[1]: Starting Advanced key-value store...
Sep 27 21:37:32 dhankar-1 systemd[1]: redis-server.service: Can't open PID file /var/run/redis/redis-server.pid (yet?) after start: No such fi
Sep 27 21:37:32 dhankar-1 systemd[1]: Started Advanced key-value store.

```
#
```
$ sudo service redis-server status
● redis-server.service - Advanced key-value store
   Loaded: loaded (/lib/systemd/system/redis-server.service; enabled; vendor preset: enabled)
   Active: inactive (dead) since Sun 2020-09-27 21:42:28 IST; 2s ago
     Docs: http://redis.io/documentation,
           man:redis-server(1)
  Process: 16430 ExecStop=/bin/kill -s TERM $MAINPID (code=exited, status=0/SUCCESS)
  Process: 15799 ExecStart=/usr/bin/redis-server /etc/redis/redis.conf (code=exited, status=0/SUCCESS)
 Main PID: 15812 (code=exited, status=0/SUCCESS)

Sep 27 21:37:32 dhankar-1 systemd[1]: Starting Advanced key-value store...
Sep 27 21:37:32 dhankar-1 systemd[1]: redis-server.service: Can't open PID file /var/run/redis/redis-server.pid (yet?) after start: No such fi
Sep 27 21:37:32 dhankar-1 systemd[1]: Started Advanced key-value store.
Sep 27 21:42:27 dhankar-1 systemd[1]: Stopping Advanced key-value store...
Sep 27 21:42:28 dhankar-1 systemd[1]: Stopped Advanced key-value store.

[2]+  Stopped                 sudo service redis-server status

```
#
```
$ redis-server
16510:C 27 Sep 21:43:58.423 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
16510:C 27 Sep 21:43:58.423 # Redis version=4.0.9, bits=64, commit=00000000, modified=0, pid=16510, just started
16510:C 27 Sep 21:43:58.423 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
16510:M 27 Sep 21:43:58.425 # You requested maxclients of 10000 requiring at least 10032 max file descriptors.
16510:M 27 Sep 21:43:58.425 # Server can't set maximum open files to 10032 because of OS error: Operation not permitted.
16510:M 27 Sep 21:43:58.425 # Current maximum open files is 4096. maxclients has been reduced to 4064 to compensate for low ulimit. If you need higher maxclients increase 'ulimit -n'.
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 4.0.9 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 16510
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           http://redis.io        
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

16510:M 27 Sep 21:43:58.425 # Server initialized
16510:M 27 Sep 21:43:58.425 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
16510:M 27 Sep 21:43:58.425 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
16510:M 27 Sep 21:43:58.425 * Ready to accept connections


```
#

#
- RQ(Redis-Queue) - https://python-rq.org/
- Source - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxii-background-jobs

> Worker processes run independently of the application and can even be located on a different system. The communication between the application and the workers is done through a message queue. The application submits a job, and then monitors its progress by interacting with the queue.

>  In cases where you want to have multiple workers to have more throughput, all you need to do is run more instances of rq worker, all connected to the same queue. Then when a job shows up in the queue, any of the available worker processes will pick it up. In a production environment you will probably want to have at least as many workers as available CPUs.

#
```

(drf_venv) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ rq worker
21:47:25 Worker rq:worker:08bb026c5e174c138ca538c738c48063: started, version 1.5.2
21:47:25 *** Listening on default...
21:47:25 Cleaning registries for queue: default

```
#