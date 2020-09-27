
```
Author from scratch

Start with a simple Hello World example.
Use a blueprint

Build a Lambda application from sample code and configuration presets for common use cases.
Browse serverless app repository

Deploy a sample Lambda application from the AWS Serverless Application Repository.
Basic information
Function name
Enter a name that describes the purpose of your function.
pyLambda
Use only letters, numbers, hyphens, or underscores with no spaces.
RuntimeInfo
Choose the language to use to write your function.
PermissionsInfo
By default, Lambda will create an execution role with permissions to upload logs to Amazon CloudWatch Logs. You can customize this default role later when adding triggers.
Change default execution role
Execution role
Choose a role that defines the permissions of your function. To create a custom role, go to the IAM console.

Create a new role with basic Lambda permissions

Use an existing role

Create a new role from AWS policy templates
Role creation might take a few minutes. Please do not delete the role or edit the trust or permissions policies in this role.
Lambda will create an execution role named pyLambda-role-sayzo2jd, with permission to upload logs to Amazon CloudWatch Logs.

CancelCreate function
```
#
```
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

```
#
```
Response:
{
  "statusCode": 200,
  "body": "\"Hello from Lambda!\""
}

Request ID:
"6daec5cd-b027-49f1-ac8e-cc258fdaa54b"

Function logs:
START RequestId: 6daec5cd-b027-49f1-ac8e-cc258fdaa54b Version: $LATEST
END RequestId: 6daec5cd-b027-49f1-ac8e-cc258fdaa54b
REPORT RequestId: 6daec5cd-b027-49f1-ac8e-cc258fdaa54b	Duration: 1.13 ms	Billed Duration: 100 ms	Memory Size: 128 MB	Max Memory Used: 52 MB	Init Duration: 117.57 ms	

```
#
