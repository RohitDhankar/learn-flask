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
- Zappa >> zappa init >> dev >> default >>  zappa-flask-s3-dhankar >> my_app.app_zappa

```
(zappa) (base) dhankar@dhankar-1:~/temp/flask/1/learn-flask/zappa$ zappa init

███████╗ █████╗ ██████╗ ██████╗  █████╗
╚══███╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
  ███╔╝ ███████║██████╔╝██████╔╝███████║
 ███╔╝  ██╔══██║██╔═══╝ ██╔═══╝ ██╔══██║
███████╗██║  ██║██║     ██║     ██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝

Welcome to Zappa!

Zappa is a system for running server-less Python web applications on AWS Lambda and AWS API Gateway.
This `init` command will help you create and configure your new Zappa deployment.
Let's get started!

Your Zappa configuration can support multiple production stages, like 'dev', 'staging', and 'production'.
What do you want to call this environment (default 'dev'): dev

AWS Lambda and API Gateway are only available in certain regions. Let's check to make sure you have a profile set up in one that will work.
We found the following profiles: default, and default_old. Which would you like us to use? (default 'default'): default

Your Zappa deployments will need to be uploaded to a private S3 bucket.
If you don't have a bucket yet, we'll create one for you too.
What do you want to call your bucket? (default 'zappa-8sedepf6v'): zappa_flask_s3
Invalid bucket name!
S3 buckets must be named according to the following rules:
* Bucket names must be unique across all existing bucket names in Amazon S3.
* Bucket names must comply with DNS naming conventions.
* Bucket names must be at least 3 and no more than 63 characters long.
* Bucket names must not contain uppercase characters or underscores.
* Bucket names must start with a lowercase letter or number.
* Bucket names must be a series of one or more labels. Adjacent labels are separated
  by a single period (.). Bucket names can contain lowercase letters, numbers, and
  hyphens. Each label must start and end with a lowercase letter or a number.
* Bucket names must not be formatted as an IP address (for example, 192.168.5.4).
* When you use virtual hosted–style buckets with Secure Sockets Layer (SSL), the SSL
  wildcard certificate only matches buckets that don't contain periods. To work around
  this, use HTTP or write your own certificate verification logic. We recommend that
  you do not use periods (".") in bucket names when using virtual hosted–style buckets.

What do you want to call your bucket? (default 'zappa-8sedepf6v'): zappa-flask-s3-dhankar

It looks like this is a Flask application.
What's the modular path to your app's function?
This will likely be something like 'your_module.app'.
We discovered: my_app.app_zappa
Where is your app's function? (default 'my_app.app_zappa'): my_app.app_zappa

You can optionally deploy to all available regions in order to provide fast global service.
If you are using Zappa for the first time, you probably don't want to do this!
Would you like to deploy this application globally? (default 'n') [y/n/(p)rimary]: n

Okay, here's your zappa_settings.json:

{
    "dev": {
        "app_function": "my_app.app_zappa",
        "aws_region": "ap-southeast-1",
        "profile_name": "default",
        "project_name": "zappa",
        "runtime": "python3.6",
        "s3_bucket": "zappa-flask-s3-dhankar"
    }
}

Does this look okay? (default 'y') [y/n]: y

Done! Now you can deploy your Zappa application by executing:

	$ zappa deploy dev

After that, you can update your application code with:

	$ zappa update dev

To learn more, check out our project page on GitHub here: https://github.com/Miserlou/Zappa
and stop by our Slack channel here: https://slack.zappa.io

Enjoy!,
 ~ Team Zappa!
(zappa) (base) dhankar@dhankar-1:~/temp/flask/1/learn-flask/zappa$ 

```
#

```
(zappa) (base) dhankar@dhankar-1:~/temp/flask/1/learn-flask/zappa$ zappa deploy dev
Calling deploy for stage dev..
Creating zappa-dev-ZappaLambdaExecutionRole IAM Role..
Creating zappa-permissions policy on zappa-dev-ZappaLambdaExecutionRole IAM Role.
Downloading and installing dependencies..
 - markupsafe==1.1.1: Downloading
100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 27.5k/27.5k [00:00<00:00, 6.41MB/s]
Packaging project as zip.
Uploading zappa-dev-1601447444.zip (5.3MiB)..
100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 5.55M/5.55M [00:01<00:00, 5.19MB/s]
Scheduling..
Scheduled zappa-dev-zappa-keep-warm-handler.keep_warm_callback with expression rate(4 minutes)!
Uploading zappa-dev-template-1601447464.json (1.6KiB)..
100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 1.61k/1.61k [00:00<00:00, 8.66kB/s]
Waiting for stack zappa-dev to create (this can take a bit)..
 75%|███████████████████████████████████████████████████████████████████████████████▌                          | 3/4 [00:12<00:04,  4.29s/res]
Deploying API Gateway..
Deployment complete!: https://khd84kp4bj.execute-api.ap-southeast-1.amazonaws.com/dev
(zappa) (base) dhankar@dhankar-1:~/temp/flask/1/learn-flask/zappa$ 

```
#
- The Zappa created LAMBDA function on AWS == zappa-dev 
- Function code >> The deployment package of your Lambda function "zappa-dev" is too large to enable inline code editing. However, you can still invoke your function.
- https://ap-southeast-1.console.aws.amazon.com/lambda/home?region=ap-southeast-1#/functions/zappa-dev?tab=configuration

```

```
#
- Copied instrcutions from the README.md for ZAPPA - 
- Zappa will automatically package up your application and local virtual environment into a Lambda-compatible archive.
- Replace any dependencies with versions precompiled for Lambda
- Set up the function handler and necessary WSGI Middleware
- Upload the archive to S3
- Create and manage necessary Amazon IAM policies and roles
- Register it as a new Lambda function
- Create a new API Gateway resource, create WSGI-compatible routes for it, link it to the new Lambda function, 
- Finally delete the archive from your S3 bucket. 

- Be aware that the default IAM role and policy created for executing Lambda applies a liberal set of permissions. These are most likely not appropriate for production deployment of important applications. See the section Custom AWS IAM Roles and Policies for Execution for more detail.
- Custom AWS IAM Roles and Policies for Execution - 

#
- Security_Remote_Env_Variables 
- Source - https://github.com/Miserlou/Zappa#custom-aws-iam-roles-and-policies-for-execution -- sensitive credentials), you can create a file and place it in an S3 bucket to which your Zappa application has access. To do this, add the remote_env key to zappa_settings pointing to a file containing a flat JSON object, so that each key-value pair on the object will be set as an environment variable and value whenever a new lambda instance spins up.

#
- S3 file upload Event tracking Lambda Func - via - zappa_settings.json file - executing-in-response-to-aws-events

- Source - https://github.com/Miserlou/Zappa/blob/93804a1b3157f0189bf062e01baab2bd4f09400d/README.md#executing-in-response-to-aws-events

- In your zappa_settings.json file, define your event sources and the function you wish to execute. For instance, this will execute ```your_module.process_upload_function``` in response to new objects in your my-bucket S3 bucket. Note that ```process_upload_function``` must accept event and context parameters.

```
{
    "production": {
       ...
       "events": [{
            "function": "your_module.process_upload_function",
            "event_source": {
                  "arn":  "arn:aws:s3:::my-bucket",
                  "events": [
                    "s3:ObjectCreated:*" // Supported event types: http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#supported-notification-event-types
                  ]
               }
            }],
       ...
    }
}

```
#
