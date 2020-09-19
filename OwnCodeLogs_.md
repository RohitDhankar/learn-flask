> Start Flask 

#

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
#

```
```

#
#

```
```

#
