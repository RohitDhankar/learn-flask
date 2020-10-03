#

```
$ sudo apt install nginx
Reading package lists... Done
Building dependency tree       
Reading state information... Done
nginx is already the newest version (1.14.0-0ubuntu1.7).
0 upgraded, 0 newly installed, 0 to remove and 25 not upgraded.

$ sudo ufw app list
Available applications:
  CUPS
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
  OpenSSH
```
#

```
    Nginx Full: This profile opens both port 80 (normal, unencrypted web traffic) and port 443 (TLS/SSL encrypted traffic)
    Nginx HTTP: This profile opens only port 80 (normal, unencrypted web traffic)
    Nginx HTTPS: This profile opens only port 443 (TLS/SSL encrypted traffic)
```
#
```
$sudo ufw allow 'Nginx HTTP'
Rules updated
Rules updated (v6)

#
$sudo ufw status
Status: inactive

# VERY PERMISIVE -- Not for Production
$ sudo ufw enable
Firewall is active and enabled on system startup

$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
22                         ALLOW       Anywhere                  
Nginx HTTP                 ALLOW       Anywhere                  
22 (v6)                    ALLOW       Anywhere (v6)             
Nginx HTTP (v6)            ALLOW       Anywhere (v6)             




```
#