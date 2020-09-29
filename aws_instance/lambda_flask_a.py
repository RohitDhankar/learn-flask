# Code from this script for the LAMBDA Func on AWS - 
# https://ap-southeast-1.console.aws.amazon.com/lambda/home?region=ap-southeast-1#/functions/flask_within_lambda?newFunction=true&tab=configuration

import boto3
import json
#import urllib3
import urllib
import flask as FLASK
from flask import Flask, render_template, request


#s3 = boto3.resource('s3')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    #print(type(event)) #<class 'dict'>
    #print(type(context)) #<class '__main__.LambdaContext'>
    # Get the bucket and object key from the Event
    bucket = event['Records'][0]['s3']['bucket']['name']
    print(type(bucket)) #<class 'dict'>
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'],encoding = 'utf-8')
    print(type(key)) 
    #Example: unquote_plus('/El+Ni%C3%B1o/') yields '/El Niño/'.
    """
    's3.ServiceResource' object has no attribute 'get_object'
    's3.ServiceResource' o
    """

    try:
        # Fetch file from S3
        response = s3.get_object(Bucket=bucket,Key=key)
        print(type(response))
        text = response['Body'].read.decode()
        data = json.loads(text)

        print(type(data))
    except Exception as excp:
        print(excp)
        # Handling exception code here - if reqd 
        raise excp

    