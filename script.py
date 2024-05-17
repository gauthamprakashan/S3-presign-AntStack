import constants 
import boto3
import requests

OBJECT_NAME_TO_UPLOAD = 'istockphoto-538665020-612x612.jpg'

s3_client = boto3.client(
    's3',
    aws_access_key_id = constants.access_key,
    aws_secret_access_key = constants.secret_access_key
)

response = s3_client.generate_presigned_post(
    Bucket = 'presign-demo1',
    Key = OBJECT_NAME_TO_UPLOAD,
    ExpiresIn = 10
)

print(response)

files = {'file':open(OBJECT_NAME_TO_UPLOAD,'rb')}
r = requests.post(response['url'],data=response['fields'],files=files)

print(r)