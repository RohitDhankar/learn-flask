> Start Flask 

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