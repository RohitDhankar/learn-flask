# Code from this script for the LAMBDA Func on AWS
import boto3
import json
s3 = boto3.resource('s3')

def lambda_handler(event, context):
    # Get the bucket and object key from the Event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    if key == 'abc/A.csv':
        'copy to Table-A from "s3:///tcm-bigdata-sandbox/Config.py"'
