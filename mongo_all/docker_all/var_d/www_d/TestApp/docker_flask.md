##### Tree structure of the DIR -- learn-flask/mongo_all/docker_all
- This file == /learn-flask/mongo_all/docker_all/var_d/www_d/TestApp/docker_flask.md
```
(base) dhankar@dhankar-1:~/learn-flask/mongo_all/docker_all$ tree
.
└── var_d
    └── www_d
        └── TestApp
            ├── app
            │   ├── __init__.py
            │   ├── static
            │   ├── template
            │   └── views.py
            └── uwsgi.ini

6 directories, 3 files
```
##### FOOBAR - Important note about the Flask Docker Image 
- 400% (4x) the performance of this image (tiangolo/uwsgi-nginx-flask)
- Source - https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask

> If you need to use Flask (instead of something based on ASGI) and you need to have the best performance possible, you can use the alternative image: tiangolo/meinheld-gunicorn-flask.

tiangolo/meinheld-gunicorn-flask will give you about 400% (4x) the performance of this image (tiangolo/uwsgi-nginx-flask).

#

```


```
#
```
```
#

