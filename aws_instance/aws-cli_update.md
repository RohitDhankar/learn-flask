- Source -- https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html

```
(base) dhankar@dhankar-1:~/temp/na/na$ aws --version
aws-cli/2.0.28 Python/3.7.3 Linux/5.4.0-48-generic botocore/2.0.0dev32
(base) dhankar@dhankar-1:~/temp/na/na$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 32.2M  100 32.2M    0     0  7981k      0  0:00:04  0:00:04 --:--:-- 7981k
(base) dhankar@dhankar-1:~/temp/na/na$ ls 
 awscliv2.zip  
(base) dhankar@dhankar-1:~/temp/na/na$ which aws
/usr/local/bin/aws
(base) dhankar@dhankar-1:~/temp/na/na$ ls -l /usr/local/bin/aws
lrwxrwxrwx 1 root root 37 Jul  4 09:11 /usr/local/bin/aws -> /usr/local/aws-cli/v2/current/bin/aws
(base) dhankar@dhankar-1:~/temp/na/na$ # got the SYM-LINK with the Command -- which aws
(base) dhankar@dhankar-1:~/temp/na/na$ # passed the SYM-LINK to the -- ls -l --- which gave the actual path 
(base) dhankar@dhankar-1:~/temp/na/na$ 

#@#sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update

(base) dhankar@dhankar-1:~/temp/na/na$ # got the SYM-LINK with the Command -- which aws
(base) dhankar@dhankar-1:~/temp/na/na$ # passed the SYM-LINK to the -- ls -l --- which gave the actual path 
(base) dhankar@dhankar-1:~/temp/na/na$ 
(base) dhankar@dhankar-1:~/temp/na/na$ ls
 aws                 awscliv2.zip                 
(base) dhankar@dhankar-1:~/temp/na/na$ sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update
[sudo] password for dhankar: 
You can now run: /usr/local/bin/aws --version
(base) dhankar@dhankar-1:~/temp/na/na$ aws --version
aws-cli/2.0.52 Python/3.7.3 Linux/5.4.0-48-generic exe/x86_64.ubuntu.18
(base) dhankar@dhankar-1:~/temp/na/na$ 

```
#

- AWS—CLI -- Configuration basics
- Source -- https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

```
(base) dhankar@dhankar-1:~/.aws$ sudo gedit credentials 
#

[default]
aws_access_key_id = A###$$$%%%^^^&&&C
aws_secret_access_key = 9R/DC###$$$%%%^^^&&&###$$$%%%^^^&&&###$$$%%%^^^&&&
```
#

```
(base) dhankar@dhankar-1:~/.aws$ sudo gedit config 
#
[default]
region = us-west-1###$$$%%%
```
#
- Updated New Credentials for IAM Users created for Dummy Testing . Copied the values from the CSV that was downloaded from >> 
- https://console.aws.amazon.com/iam/home?region=ap-southeast-1#/users/MyUser?section=security_credentials

```
(base) dhankar@dhankar-1:~/.aws$ sudo gedit credentials
#
(base) dhankar@dhankar-1:~/.aws$ sudo gedit config

[default]
region = ap-southeast-1

```


#
- You can use roles to delegate access to users, applications, or services that don't normally have access to your AWS resources. 
- For example, you might want to grant users in your AWS account access to resources they don't usually have, or grant users in one AWS account access to resources in another account. 
- Mobile App - Or you might want to allow a mobile app to use AWS resources, but not want to embed AWS keys within the app (where they can be difficult to rotate and where users can potentially extract them). 
- Active Directory -- Sometimes you want to give AWS access to users who already have identities defined outside of AWS, such as in your corporate directory. Or, you might want to grant access to your account to third parties so that they can perform an audit on your resources. 

```
```
#

#

```
S3()                                                                      S3()

NAME
       s3 -

DESCRIPTION
       This  section  explains  prominent concepts and notations in the set of
       high-level S3 commands provided.

   Path Argument Type
       Whenever using a command, at least one path argument must be specified.
       There are two types of path arguments: LocalPath and S3Uri.

       LocalPath: represents the path of a local file or directory.  It can be
       written as an absolute path or relative path.

       S3Uri: represents the location of a S3 object, prefix, or bucket.  This
       must  be  written in the form s3://mybucket/mykey where mybucket is the
       specified S3 bucket, mykey is the specified S3 key.  The path  argument
       must  begin with s3:// in order to denote that the path argument refers
       to a S3 object. Note that prefixes are separated  by  forward  slashes.
       For  example, if the S3 object myobject had the prefix myprefix, the S3
       key would be myprefix/myobject, and if the object  was  in  the  bucket
       mybucket, the S3Uri would be s3://mybucket/myprefix/myobject.

       S3Uri  also supports S3 access points. To specify an access point, this
       value must be of the form s3://<access-point-arn>/<key>. For example if
       the   access   point   myaccesspoint   to   be   used   has   the  ARN:
       arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint   and   the
       object  being  accessed has the key mykey, then the S3URI used must be:
       s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mykey.
       Similar  to  bucket  names, you can also use prefixes with access point
       ARNs        for         the         S3Uri.         
       For         example:
       s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mypre-
       fix/

    The higher level s3 commands do not support access point  object  ARNs.
       For      example,      if      the     following     was     specified:
       s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccess-
       point/object/mykey   the   S3URI   will   resolve  to  the  object  key
       object/mykey

   Order of Path Arguments
       Every command takes one or two positional path  arguments.   The  first
       path  argument represents the source, which is the local file/directory
       or S3 object/prefix/bucket that is being referenced.   
       
       If  there  is  a second path argument, it represents the destination, which is the local
       file/directory or S3 object/prefix/bucket that is  being  operated  on.
       Commands  with only one path argument do not have a destination because
       the operation is being performed only on the source.

   Single Local File and S3 Object Operations


```
#

#

```
(base) dhankar@dhankar-1:~/temp/na/na$ aws iam create-group --group-name MyIamGroup
{
    "Group": {
        "Path": "/",
        "GroupName": "MyIamGroup",
        "GroupId": "AGPAZEVMGDREKJVV5AMTK",
        "Arn": "arn:aws:iam::628500077650:group/MyIamGroup",
        "CreateDate": "2020-09-27T11:22:45+00:00"
    }
}
(base) dhankar@dhankar-1:~/temp/na/na$ aws iam create-user --user-name MyUser
{
    "User": {
        "Path": "/",
        "UserName": "MyUser",
        "UserId": "AIDAZEVMGDREB7QFKPTHW",
        "Arn": "arn:aws:iam::628500077650:user/MyUser",
        "CreateDate": "2020-09-27T11:23:51+00:00"
    }
}
(base) dhankar@dhankar-1:~/temp/na/na$ aws iam add-user-to-group --user-name MyUser --group-name MyIamGroup
(base) dhankar@dhankar-1:~/temp/na/na$ aws iam get-group --group-name MyIamGroup
{
    "Users": [
        {
            "Path": "/",
            "UserName": "MyUser",
            "UserId": "AIDAZEVMGDREB7QFKPTHW",
            "Arn": "arn:aws:iam::628500077650:user/MyUser",
            "CreateDate": "2020-09-27T11:23:51+00:00"
        }
    ],
    "Group": {
        "Path": "/",
        "GroupName": "MyIamGroup",
        "GroupId": "AGPAZEVMGDREKJVV5AMTK",
        "Arn": "arn:aws:iam::628500077650:group/MyIamGroup",
        "CreateDate": "2020-09-27T11:22:45+00:00"
    }
}
(base) dhankar@dhankar-1:~/temp/na/na$ aws iam create-user --user-name MyUser2
{
    "User": {
        "Path": "/",
        "UserName": "MyUser2",
        "UserId": "AIDAZEVMGDRECYR2D5AJP",
        "Arn": "arn:aws:iam::628500077650:user/MyUser2",
        "CreateDate": "2020-09-27T11:25:12+00:00"
    }
}
(base) dhankar@dhankar-1:~/temp/na/na$ aws iam add-user-to-group --user-name MyUser2 --group-name MyIamGroup
(base) dhankar@dhankar-1:~/temp/na/na$ aws iam get-group --group-name MyIamGroup
{
    "Users": [
        {
            "Path": "/",
            "UserName": "MyUser",
            "UserId": "AIDAZEVMGDREB7QFKPTHW",
            "Arn": "arn:aws:iam::628500077650:user/MyUser",
            "CreateDate": "2020-09-27T11:23:51+00:00"
        },
        {
            "Path": "/",
            "UserName": "MyUser2",
            "UserId": "AIDAZEVMGDRECYR2D5AJP",
            "Arn": "arn:aws:iam::628500077650:user/MyUser2",
            "CreateDate": "2020-09-27T11:25:12+00:00"
        }
    ],
    "Group": {
        "Path": "/",
        "GroupName": "MyIamGroup",
        "GroupId": "AGPAZEVMGDREKJVV5AMTK",
        "Arn": "arn:aws:iam::628500077650:group/MyIamGroup",
        "CreateDate": "2020-09-27T11:22:45+00:00"
    }
}
(base) dhankar@dhankar-1:~/temp/na/na$ 

```
#

#
- ARN - Amazon Resource Name (ARN)
```
arn:aws:s3:::elasticbeanstalk-ap-southeast-1-628500077650
```
#
#
> 

When you use aws s3 commands to upload large objects to an Amazon S3 bucket, the AWS CLI automatically performs a multipart upload. You can't resume a failed upload when using these aws s3 commands.

If the multipart upload fails due to a timeout, or if you manually canceled in the AWS CLI, the AWS CLI stops the upload and cleans up any files that were created. This process can take several minutes.

If the multipart upload or cleanup process is canceled by a kill command or system failure, the created files remain in the Amazon S3 bucket. To clean up the multipart upload, use the s3api abort-multipart-upload command.

For more information, see Multipart upload overview in the Amazon Simple Storage Service Developer Guide.


```
```
#
```
Amazon S3/elasticbeanstalk-ap-southeast-1-628500077650
elasticbeanstalk-ap-southeast-1-628500077650
Buckets are globally unique containers for everything that you store in Amazon S3.	After you create a bucket, you can upload your objects (for example, your photo or video files).	By default, the permissions on an object are private, but you can set up access control policies to grant permissions to others.
Review
1 Files Size: 128.0 KB Target path: elasticbeanstalk-ap-southeast-1-628500077650
Storage class
Choose a storage class based on your use case and access requirements. Learn more  or see Amazon S3 pricing 

Storage class	Designed for	Availability Zones	Min storage duration	Min billable object size	Monitoring and automation fees	Retrieval fees
Standard	Frequently accessed data	≥ 3	-	-	-	-
Intelligent-Tiering	Long-lived data with changing or unknown access patterns	≥ 3	30 days	-	Per-object fees apply	-
Standard-IA	Long-lived, infrequently accessed data	≥ 3	30 days	128KB	-	Per-GB fees apply
One Zone-IA	Long-lived, infrequently accessed, non-critical data	≥ 1	30 days	128KB	-	Per-GB fees apply
Glacier	Archive data with retrieval times ranging from minutes to hours	≥ 3	90 days	40KB	-	Per-GB fees apply
Glacier Deep Archive	Archive data that rarely, if ever, needs to be accessed with retrieval times in hours	≥ 3	180 days	40KB	-	Per-GB fees apply
Reduced Redundancy (Not recommended)	Frequently accessed, non-critical data	≥ 3	-	-	-	-
Encryption

```
#
- uploaded a PDF file - from the Browser ( lame browser drag and drop upload )
```
(base) dhankar@dhankar-1:~/temp/na/na$ aws s3 ls
2020-06-13 00:50:44 elasticbeanstalk-ap-southeast-1-628500077650
(base) dhankar@dhankar-1:~/temp/na/na$ aws s3 ls elasticbeanstalk-ap-southeast-1-628500077650

# Above command gives no File DIR Structure as no Files uploaded yet ...

(base) dhankar@dhankar-1:~/temp/na/na$ aws s3 ls elasticbeanstalk-ap-southeast-1-628500077650
2020-09-27 19:41:53     131087 Lead_Data Scientist _MachineLearning(1).pdf
#


```
#
- (AccessDenied) when calling the DeleteBucket operation: Access Denied
```
$ aws s3 rb s3://elasticbeanstalk-ap-southeast-1-628500077650 --force
delete: s3://elasticbeanstalk-ap-southeast-1-628500077650/Lead_Data Scientist _MachineLearning(1).pdf
remove_bucket failed: s3://elasticbeanstalk-ap-southeast-1-628500077650 An error occurred (AccessDenied) when calling the DeleteBucket operation: Access Denied

```
#
- Delete Bucket which has content within it , need to use the Flag -- force 
- The Bucket Policy needs to be Updated in the AWS Console before we can Delete the bucket from the AWS-CLI
- https://s3.console.aws.amazon.com/s3/buckets/elasticbeanstalk-ap-southeast-1-628500077650/?region=ap-southeast-1&tab=permissions
#
- below change the value to - "Allow" for the key -- "Effect": "Deny", coreesponding to the Key - "Action": "s3:DeleteBucket",
#
```
{
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "eb-ad78f54a-f239-4c90-adda-49e5f56cb51e",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::628500077650:role/aws-elasticbeanstalk-ec2-role"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::elasticbeanstalk-ap-southeast-1-628500077650/resources/environments/logs/*"
        },
        {
            "Sid": "eb-af163bf3-d27b-4712-b795-d1e33e331ca4",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::628500077650:role/aws-elasticbeanstalk-ec2-role"
            },
            "Action": [
                "s3:ListBucketVersions",
                "s3:ListBucket",
                "s3:GetObjectVersion",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::elasticbeanstalk-ap-southeast-1-628500077650",
                "arn:aws:s3:::elasticbeanstalk-ap-southeast-1-628500077650/resources/environments/*"
            ]
        },
        {
            "Sid": "eb-58950a8c-feb6-11e2-89e0-0800277d041b",
            "Effect": "Deny", # CHANGE THIS TO "Allow"
            "Principal": {
                "AWS": "*"
            },
            "Action": "s3:DeleteBucket",
            "Resource": "arn:aws:s3:::elasticbeanstalk-ap-southeast-1-628500077650"
        }
    ]
}

```
#
- As seen below Bucket S3 Deleted - 
#
```
$ aws s3 rb s3://elasticbeanstalk-ap-southeast-1-628500077650 --force
remove_bucket: elasticbeanstalk-ap-southeast-1-628500077650

```
#

#
- Name and Create a New Bucket in S3 - follow Naming Rules as seen at below link 
- https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-s3-bucket-naming-requirements.html
```
$ aws s3 mb s3://bucketdummystarted
make_bucket: bucketdummystarted

```
#
- Make S3 Buckets to test with Lambda Function
```
(base) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ aws s3 mb s3://bucketpythonlambdatest
make_bucket: bucketpythonlambdatest
(base) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ aws s3 mb s3://bucketpythonlambdatest1
make_bucket: bucketpythonlambdatest1
(base) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ aws s3 mb s3://bucketpythonlambdatest2
make_bucket: bucketpythonlambdatest2
(base) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ 

```
#
- 2 New IAM Roles Created - one as part of the LAMBDA Function creation another for testing File Uploads from the AWS-CLI
#
- IAM Role ARN - arn:aws:iam::628500077640:role/lambda_s3_1
#
```
(base) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ aws s3 cp redis-server.md  s3://bucketpythonlambdatest
upload: ./redis-server.md to s3://bucketpythonlambdatest/redis-server.md
(base) dhankar@dhankar-1:~/temp/flask/1/learn-flask$ aws s3 ls bucketpythonlambdatest
2020-09-28 00:15:09       7508 redis-server.md

```
#
- Now change the IAM Role from the AWS-CLI and upload other Files and List the Contents of the Bucket with the command - aws s3 cp - AND - aws s3 ls

#
- FOOBAR_Errors as seen below after Deleting Default IAM user and trying to Upload Files in SUB DIR from another IAM User 
```
$ aws s3 cp redis-server.md  s3://bucketpythonlambdatest/csv_files/
upload failed: ./redis-server.md to s3://bucketpythonlambdatest/csv_files/redis-server.md An error occurred (InvalidAccessKeyId) when calling the PutObject operation: The AWS Access Key Id you provided does not exist in our records.
# Above Solved by Adding new credentials in the - credentials and Config files 
#
$ cd ~/.aws
(base) dhankar@dhankar-1:~/.aws$ ls -ltr
total 8
-rw------- 1 dhankar dhankar 116 Jul  4 10:57 credentials
-rw------- 1 dhankar dhankar  29 Jul  4 11:48 config

```
#
#
- FOOBAR_Error as seen below after Deleting Default IAM user and trying to Upload Files in SUB DIR from another IAM User 
```
$ aws s3 cp redis-server.md  s3://bucketpythonlambdatest/csv_files/
upload failed: ./redis-server.md to s3://bucketpythonlambdatest/csv_files/redis-server.md An error occurred (AccessDenied) when calling the PutObject operation: Access Denied
```
- Above Error -Solved for now by adding the New IAM User to the ADMIN GROUP = https://console.aws.amazon.com/iam/home?region=ap-southeast-1#/groups/AdminDhankarGroupJul2020
- https://console.aws.amazon.com/iam/home?region=ap-southeast-1#/groups/AdminDhankarGroupJul2020
- This is not the best possible solution - FOOBAR ( UPDATE)
#
#
```
$ aws s3 cp redis-server.md  s3://bucketpythonlambdatest/csv_files/
upload: ./redis-server.md to s3://bucketpythonlambdatest/csv_files/redis-server.md
```
#
#
- FOOBAR_ERROR as seen below while creating the LAMBDA FUNC
- The notification destination service region is not valid for the bucket location constraint
- ScreenCapture of the ERROR == 
- Solved by changing REGION of S3 Buckets - to be same as REGION of the LAMBDA FUNC's
```
```
#
#
- FOOBAR - Note to self , had created 4 Buckets in the Regio US -West 
- https://s3.console.aws.amazon.com/s3/home?region=us-west-1
- Delete these buckets in case they incurr billing - the LAMBDA functions are  being now coded in the region=ap-southeast-1 , as the new IAM users were created in - region=ap-southeast-1
```
$ aws s3 mb s3://bucket-lambda-func-test
make_bucket: bucket-lambda-func-test

```
#
#
- Upload CSV file into Object Location ( psudo SUB DIR ) -s3://bucket-lambda-func-test/csv_files/ , for LAMBDA Func 
```
aws s3 cp ~/temp/aws_instance/data/mtcars.csv  s3://bucket-lambda-func-test/csv_files/
upload: ./mtcars.csv to s3://bucket-lambda-func-test/csv_files/mtcars.csv
```
#
#
- The LAMBDA Func and the S3 Bucket ( SUB DIR ) - s3://bucket-lambda-func-test/csv_files/ , have been linked ( associated with each other)

- https://ap-southeast-1.console.aws.amazon.com/lambda/home?region=ap-southeast-1#/functions/S3GetObjects?tab=configuration
- below text is manually copied from the GUI of AWS at above URL

```
S3: bucket-lambda-func-test (Enabled)
arn:aws:s3:::bucket-lambda-func-test
Details
Event type: ObjectCreatedByPut
Notification name: S3_ObjectPUT_Event
Prefix: csv_files/
Suffix: .csv

```
#
- test 
- aws lambda invoke --function-name S3GetObjects  --invocation-type Event --payload '{ "key": "value" }' response.json
{
    "StatusCode": 202
}
#
```
{'ResponseMetadata': 

{'RequestId': 'AF1C9BB9E98D8DF4', 'HostId': 'F442SsC3VTwRandLwLgBkDtIjRTTOTuGttXSlB048C427Rp9Mk/IQGlTOmnImwbweCcEugSVZT4=', 'HTTPStatusCode': 200, 

'HTTPHeaders': 
{'x-amz-id-2': 'F442SsC3VTwRandLwLgBkDtIjRTTOTuGttXSlB048C427Rp9Mk/IQGlTOmnImwbweCcEugSVZT4=', 'x-amz-request-id': 'AF1C9BB9E98D8DF4', 'date': 'Mon, 28 Sep 2020 10:43:34 GMT', 'last-modified': 'Mon, 28 Sep 2020 10:43:31 GMT', 'etag': '"c502359c26a0931eef53b2207b2344f9"', 'accept-ranges': 'bytes', 'content-type': 'text/csv', 'content-length': '1700', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 
'AcceptRanges': 'bytes', 
'LastModified': datetime.datetime(2020, 9, 28, 10, 43, 31, tzinfo=tzutc()), 
'ContentLength': 1700, 
'ETag': '"c502359c26a0931eef53b2207b2344f9"', 
'ContentType': 'text/csv', 'Metadata': {}, 
'Body': <botocore.response.StreamingBody object at 0x7f7a50959be0>}

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
