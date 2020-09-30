#import boto3
#import json
#import urllib3
#import urllib

from flask import Flask #, render_template, request

app_zappa = Flask(__name__)

@app_zappa.route('/')
def test_zappa():
    return "hello from zappa flask app on aws lambda"

if __name__ == "__main__":
    app_zappa.run(debug=True)  

