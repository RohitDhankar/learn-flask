##### ZAPPA 
- https://github.com/Miserlou/Zappa#about

Other option to be tried next -- https://github.com/logandk/serverless-wsgi
Just going by STARS - ZAPPA = 11,000 + 
serveless-wsgi = 360 + 


#

```
$ pip install zappa
Collecting zappa
  Downloading zappa-0.51.0-py3-none-any.whl (114 kB)
     |████████████████████████████████| 114 kB 4.4 MB/s 
Collecting python-dateutil<2.7.0
  Downloading python_dateutil-2.6.1-py2.py3-none-any.whl (194 kB)
     |████████████████████████████████| 194 kB 76.2 MB/s 
Collecting pip-tools
  Downloading pip_tools-5.3.1-py2.py3-none-any.whl (45 kB)
     |████████████████████████████████| 45 kB 408 kB/s 
Processing /home/dhankar/.cache/pip/wheels/13/90/db/290ab3a34f2ef0b5a0f89235dc2d40fea83e77de84ed2dc05c/PyYAML-5.3.1-cp38-cp38-linux_x86_64.whl
Collecting toml
  Using cached toml-0.10.1-py2.py3-none-any.whl (19 kB)
Collecting boto3
  Downloading boto3-1.15.8-py2.py3-none-any.whl (129 kB)
     |████████████████████████████████| 129 kB 114.6 MB/s 
Collecting troposphere
  Downloading troposphere-2.6.2.tar.gz (179 kB)
     |████████████████████████████████| 179 kB 93.7 MB/s 
Collecting wsgi-request-logger
  Downloading wsgi-request-logger-0.4.6.tar.gz (4.4 kB)
Requirement already satisfied: wheel in /home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages (from zappa) (0.34.2)
Collecting Werkzeug<1.0
  Downloading Werkzeug-0.16.1-py2.py3-none-any.whl (327 kB)
     |████████████████████████████████| 327 kB 28.4 MB/s 
Collecting python-slugify
  Downloading python-slugify-4.0.1.tar.gz (11 kB)
Collecting durationpy
  Downloading durationpy-0.5.tar.gz (1.7 kB)
Collecting tqdm
  Downloading tqdm-4.50.0-py2.py3-none-any.whl (70 kB)
     |████████████████████████████████| 70 kB 1.5 MB/s 
Requirement already satisfied: pip>=9.0.1 in /home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages (from zappa) (20.1.1)
Collecting kappa==0.6.0
  Downloading kappa-0.6.0.tar.gz (29 kB)
Collecting hjson
  Downloading hjson-3.0.2-py3-none-any.whl (54 kB)
     |████████████████████████████████| 54 kB 337 kB/s 
Collecting argcomplete
  Downloading argcomplete-1.12.1-py2.py3-none-any.whl (38 kB)
Requirement already satisfied: requests>=2.20.0 in /home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages (from zappa) (2.24.0)
Processing /home/dhankar/.cache/pip/wheels/8e/70/28/3d6ccd6e315f65f245da085482a2e1c7d14b90b30f239e2cf4/future-0.18.2-py3-none-any.whl
Collecting jmespath
  Downloading jmespath-0.10.0-py2.py3-none-any.whl (24 kB)
Requirement already satisfied: six in /home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages (from zappa) (1.15.0)
Requirement already satisfied: click>=7 in /home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages (from pip-tools->zappa) (7.1.2)
Collecting s3transfer<0.4.0,>=0.3.0
  Downloading s3transfer-0.3.3-py2.py3-none-any.whl (69 kB)
     |████████████████████████████████| 69 kB 765 kB/s 
Collecting botocore<1.19.0,>=1.18.8
  Downloading botocore-1.18.8-py2.py3-none-any.whl (6.6 MB)
     |████████████████████████████████| 6.6 MB 77.4 MB/s 
Collecting cfn_flip>=1.0.2
  Downloading cfn_flip-1.2.3.tar.gz (10 kB)
Collecting text-unidecode>=1.3
  Downloading text_unidecode-1.3-py2.py3-none-any.whl (78 kB)
     |████████████████████████████████| 78 kB 941 kB/s 
Collecting placebo>=0.8.1
  Downloading placebo-0.9.0.tar.gz (13 kB)
Requirement already satisfied: certifi>=2017.4.17 in /home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages (from requests>=2.20.0->zappa) (2020.6.20)
Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages (from requests>=2.20.0->zappa) (1.25.10)
Requirement already satisfied: chardet<4,>=3.0.2 in /home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages (from requests>=2.20.0->zappa) (3.0.4)
Requirement already satisfied: idna<3,>=2.5 in /home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages (from requests>=2.20.0->zappa) (2.10)
Building wheels for collected packages: troposphere, wsgi-request-logger, python-slugify, durationpy, kappa, cfn-flip, placebo
  Building wheel for troposphere (setup.py) ... done
  Created wheel for troposphere: filename=troposphere-2.6.2-py3-none-any.whl size=178050 sha256=cc1c614dbc434022a091887b84339d5686222dba6ddf5956db5e367cc6d0fb1d
  Stored in directory: /home/dhankar/.cache/pip/wheels/ed/92/62/f0d84abd67a138cc73c6520ada366d051c93367df146ead476
  Building wheel for wsgi-request-logger (setup.py) ... done
  Created wheel for wsgi-request-logger: filename=wsgi_request_logger-0.4.6-py3-none-any.whl size=4208 sha256=5bcc4a940a8bb4aad49e27b76affc0d7762a88cb467663685ec60ef16fc1d3af
  Stored in directory: /home/dhankar/.cache/pip/wheels/32/f7/fa/e13906a2b820209f9f9367e900e499d464f7e73bb8c9598254
  Building wheel for python-slugify (setup.py) ... done
  Created wheel for python-slugify: filename=python_slugify-4.0.1-py2.py3-none-any.whl size=6767 sha256=479c726702233b94850cd4e78e1e024837bcb969ba58d72351ceb3a351e99f95
  Stored in directory: /home/dhankar/.cache/pip/wheels/91/4d/4f/e740a68c215791688c46c4d6251770a570e8dfea91af1acb5c
  Building wheel for durationpy (setup.py) ... done
  Created wheel for durationpy: filename=durationpy-0.5-py3-none-any.whl size=2514 sha256=ae8eddf06bd33f0ea99e478201d1043631fda6062d736ba55b71c4839d49f2d5
  Stored in directory: /home/dhankar/.cache/pip/wheels/dd/01/04/4d1a797deac1a392c51d8ac102746af685f7d21e6e466502ca
  Building wheel for kappa (setup.py) ... done
  Created wheel for kappa: filename=kappa-0.6.0-py3-none-any.whl size=34690 sha256=09f33fe7db95b2000346c034ba084e6b2f9fc64180e439c864b71f395bb27e56
  Stored in directory: /home/dhankar/.cache/pip/wheels/14/55/09/a4ad81f6b6ca3978c9fd4309956b5eebd8ada33935202db46a
  Building wheel for cfn-flip (setup.py) ... done
  Created wheel for cfn-flip: filename=cfn_flip-1.2.3-py3-none-any.whl size=15150 sha256=b7d3469589170a51d0a2030761d7ade58ce32c0e9cef081883de72f840b6dbe3
  Stored in directory: /home/dhankar/.cache/pip/wheels/cb/bd/7d/6ed361a7ae2df71275c5d1f7cd008360ae3e2b28f47da6cc78
  Building wheel for placebo (setup.py) ... done
  Created wheel for placebo: filename=placebo-0.9.0-py3-none-any.whl size=14795 sha256=1d81a34b720a0ebf5a4eba47bc87ff3bdf0d3e33dbb9c51ea02ed5ae08730c92
  Stored in directory: /home/dhankar/.cache/pip/wheels/a4/f1/39/79934c8ef89815b46f0128bf35c34bfcdebc638ce73b2bbbdd
Successfully built troposphere wsgi-request-logger python-slugify durationpy kappa cfn-flip placebo
ERROR: pandas 1.1.1 has requirement python-dateutil>=2.7.3, but you'll have python-dateutil 2.6.1 which is incompatible.
Installing collected packages: python-dateutil, pip-tools, PyYAML, toml, jmespath, botocore, s3transfer, boto3, cfn-flip, troposphere, wsgi-request-logger, Werkzeug, text-unidecode, python-slugify, durationpy, tqdm, placebo, kappa, hjson, argcomplete, future, zappa
  Attempting uninstall: python-dateutil
    Found existing installation: python-dateutil 2.8.1
    Uninstalling python-dateutil-2.8.1:
      Successfully uninstalled python-dateutil-2.8.1
  Attempting uninstall: Werkzeug
    Found existing installation: Werkzeug 1.0.1
    Uninstalling Werkzeug-1.0.1:
      Successfully uninstalled Werkzeug-1.0.1
Successfully installed PyYAML-5.3.1 Werkzeug-0.16.1 argcomplete-1.12.1 boto3-1.15.8 botocore-1.18.8 cfn-flip-1.2.3 durationpy-0.5 future-0.18.2 hjson-3.0.2 jmespath-0.10.0 kappa-0.6.0 pip-tools-5.3.1 placebo-0.9.0 python-dateutil-2.6.1 python-slugify-4.0.1 s3transfer-0.3.3 text-unidecode-1.3 toml-0.10.1 tqdm-4.50.0 troposphere-2.6.2 wsgi-request-logger-0.4.6 zappa-0.51.0
```
#

- i am currently using a CONDA venv -- Zappa team recommends - https://docs.python-guide.org/dev/virtualenvs/


```
$ zappa init
/home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages/setuptools/distutils_patch.py:25: UserWarning: Distutils was imported before Setuptools. This usage is discouraged and may exhibit undesirable behaviors or errors. Please use Setuptools' objects directly or at least import Setuptools first.
  warnings.warn(
Oh no! An error occurred! :(

==============

Traceback (most recent call last):
  File "/home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages/zappa/cli.py", line 2778, in handle
    sys.exit(cli.handle())
  File "/home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages/zappa/cli.py", line 483, in handle
    self.init()
  File "/home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages/zappa/cli.py", line 1569, in init
    self.check_venv()
  File "/home/dhankar/anaconda3/envs/drf_venv/lib/python3.8/site-packages/zappa/cli.py", line 2686, in check_venv
    raise ClickException(
click.exceptions.ClickException: Zappa requires an active virtual environment!
Learn more about virtual environments here: http://docs.python-guide.org/en/latest/dev/virtualenvs/

==============

Need help? Found a bug? Let us know! :D
File bug reports on GitHub here: https://github.com/Miserlou/Zappa
And join our Slack channel here: https://slack.zappa.io
Love!,
 ~ Team Zappa!

```
#
- Installed -- pipenv 
- when activated - (zappa)(base) - why do we get (base)
#
```
dhankar@dhankar-1:~/temp/flask/1/learn-flask/zappa$ pip install --user pipenv
Collecting pipenv
  Downloading pipenv-2020.8.13-py2.py3-none-any.whl (3.9 MB)
     |████████████████████████████████| 3.9 MB 4.2 MB/s 
Requirement already satisfied: virtualenv-clone>=0.2.5 in /home/dhankar/.local/lib/python3.6/site-packages (from pipenv) (0.5.4)
Requirement already satisfied: virtualenv in /usr/local/lib/python3.6/dist-packages (from pipenv) (20.0.5)
Requirement already satisfied: pip>=18.0 in /usr/local/lib/python3.6/dist-packages (from pipenv) (20.0.2)
Requirement already satisfied: setuptools>=36.2.1 in /usr/lib/python3/dist-packages (from pipenv) (39.0.1)
Requirement already satisfied: certifi in /home/dhankar/.local/lib/python3.6/site-packages (from pipenv) (2019.11.28)
Requirement already satisfied: importlib-resources<2,>=1.0; python_version < "3.7" in /usr/local/lib/python3.6/dist-packages (from virtualenv->pipenv) (1.0.2)
Requirement already satisfied: appdirs<2,>=1.4.3 in /usr/local/lib/python3.6/dist-packages (from virtualenv->pipenv) (1.4.3)
Requirement already satisfied: distlib<1,>=0.3.0 in /usr/local/lib/python3.6/dist-packages (from virtualenv->pipenv) (0.3.0)
Requirement already satisfied: filelock<4,>=3.0.0 in /usr/local/lib/python3.6/dist-packages (from virtualenv->pipenv) (3.0.12)
Requirement already satisfied: six<2,>=1.9.0 in /usr/lib/python3/dist-packages (from virtualenv->pipenv) (1.11.0)
Requirement already satisfied: importlib-metadata<2,>=0.12; python_version < "3.8" in /home/dhankar/.local/lib/python3.6/site-packages (from virtualenv->pipenv) (1.7.0)
Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.6/dist-packages (from importlib-metadata<2,>=0.12; python_version < "3.8"->virtualenv->pipenv) (3.0.0)
Installing collected packages: pipenv
Successfully installed pipenv-2020.8.13
WARNING: You are using pip version 20.0.2; however, version 20.2.3 is available.
You should consider upgrading via the '/usr/bin/python3 -m pip install --upgrade pip' command.
dhankar@dhankar-1:~/temp/flask/1/learn-flask/zappa$ pipenv install flask
Creating a virtualenv for this project…
Pipfile: /home/dhankar/temp/flask/1/learn-flask/zappa/Pipfile
Using /usr/bin/python3 (3.6.9) to create virtualenv…
⠏ Creating virtual environment...created virtual environment CPython3.6.9.final.0-64 in 1790ms
  creator CPython3Posix(dest=/home/dhankar/.virtualenvs/zappa-aLRHj4VL, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/home/dhankar/.local/share/virtualenv/seed-v1)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

✔ Successfully created virtual environment! 
Virtualenv location: /home/dhankar/.virtualenvs/zappa-aLRHj4VL
Creating a Pipfile for this project…
Installing flask…
Adding flask to Pipfile's [packages]…
✔ Installation Succeeded 
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Building requirements...
Resolving dependencies...
✔ Success! 
Updated Pipfile.lock (8a3288)!
Installing dependencies from Pipfile.lock (8a3288)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
dhankar@dhankar-1:~/temp/flask/1/learn-flask/zappa$ pipenv shell
Launching subshell in virtual environment…
 . /home/dhankar/.virtualenvs/zappa-aLRHj4VL/bin/activate
(base) dhankar@dhankar-1:~/temp/flask/1/learn-flask/zappa$  . /home/dhankar/.virtualenvs/zappa-aLRHj4VL/bin/activate
(zappa) (base) dhankar@dhankar-1:~/temp/flask/1/learn-flask/zappa$ 
(zappa) (base) dhankar@dhankar-1:~/temp/flask/1/learn-flask/zappa$ 

```
#
- have the Pipfile and Pipfile.lock -- within this DIR , do these need to be GitIgnored ? 
- https://stackoverflow.com/a/46303305/4928635
> The lock file tells pipenv exactly which version of each dependency needs to be installed. You will have consistency across all machines.

```
(zappa) (base) dhankar@dhankar-1:~/temp/flask/1/learn-flask/zappa$ tree
.
├── my_app.py
├── Pipfile
├── Pipfile.lock
├── reqmts_pipenv_zappa.txt
├── zappa_codeLogs.md
└── zappa_settings.json

0 directories, 6 files
(zappa) (base) dhankar@dhankar-1:~/temp/flask/1/learn-flask/zappa$ 

```
#