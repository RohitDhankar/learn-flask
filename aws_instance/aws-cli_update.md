- Source -- https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html

```
(base) dhankar@dhankar-1:~/temp/na/na$ aws --version
aws-cli/2.0.28 Python/3.7.3 Linux/5.4.0-48-generic botocore/2.0.0dev32
(base) dhankar@dhankar-1:~/temp/na/na$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 32.2M  100 32.2M    0     0  7981k      0  0:00:04  0:00:04 --:--:-- 7981k
(base) dhankar@dhankar-1:~/temp/na/na$ ls 
 awscliv2.zip  'Means of file transfer (1).docx'  'METHODS TO PUT FILES ON AWS S3.docx'   s3-dg.pdf  'Uploading Files on S3 (1).docx'
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
 aws                 awscliv2.zip                      'METHODS TO PUT FILES ON AWS S3.docx'  'Uploading Files on S3 (1).docx'
 aws-cli_update.md  'Means of file transfer (1).docx'   s3-dg.pdf
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
aws_access_key_id = AKIAZEVMGDRENYGLXUWC
aws_secret_access_key = 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
```
#

```
(base) dhankar@dhankar-1:~/.aws$ sudo gedit config 
#
[default]
region = us-west-1
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
        "Arn": "arn:aws:iam::628500077640:group/MyIamGroup",
        "CreateDate": "2020-09-27T11:22:45+00:00"
    }
}
(base) dhankar@dhankar-1:~/temp/na/na$ aws iam create-user --user-name MyUser
{
    "User": {
        "Path": "/",
        "UserName": "MyUser",
        "UserId": "AIDAZEVMGDREB7QFKPTHW",
        "Arn": "arn:aws:iam::628500077640:user/MyUser",
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
            "Arn": "arn:aws:iam::628500077640:user/MyUser",
            "CreateDate": "2020-09-27T11:23:51+00:00"
        }
    ],
    "Group": {
        "Path": "/",
        "GroupName": "MyIamGroup",
        "GroupId": "AGPAZEVMGDREKJVV5AMTK",
        "Arn": "arn:aws:iam::628500077640:group/MyIamGroup",
        "CreateDate": "2020-09-27T11:22:45+00:00"
    }
}
(base) dhankar@dhankar-1:~/temp/na/na$ aws iam create-user --user-name MyUser2
{
    "User": {
        "Path": "/",
        "UserName": "MyUser2",
        "UserId": "AIDAZEVMGDRECYR2D5AJP",
        "Arn": "arn:aws:iam::628500077640:user/MyUser2",
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
            "Arn": "arn:aws:iam::628500077640:user/MyUser",
            "CreateDate": "2020-09-27T11:23:51+00:00"
        },
        {
            "Path": "/",
            "UserName": "MyUser2",
            "UserId": "AIDAZEVMGDRECYR2D5AJP",
            "Arn": "arn:aws:iam::628500077640:user/MyUser2",
            "CreateDate": "2020-09-27T11:25:12+00:00"
        }
    ],
    "Group": {
        "Path": "/",
        "GroupName": "MyIamGroup",
        "GroupId": "AGPAZEVMGDREKJVV5AMTK",
        "Arn": "arn:aws:iam::628500077640:group/MyIamGroup",
        "CreateDate": "2020-09-27T11:22:45+00:00"
    }
}
(base) dhankar@dhankar-1:~/temp/na/na$ 

```
#

#
- ARN - Amazon Resource Name (ARN)
```
arn:aws:s3:::elasticbeanstalk-ap-southeast-1-628500077640
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
