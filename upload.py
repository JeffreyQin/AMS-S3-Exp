import os
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

def upload_file(file_path, bucket_name, obj_name):
    try:
        s3.upload_file(file_path, bucket_name, obj_name)
        print('upload success')
    except ClientError:
        print('upload error')

file_path = 'test_upload_data/test.csv'
bucket_name = 'watolink-bucket-1'
obj_name = 's3://test_folder/test.csv'
upload_file(file_path, bucket_name, obj_name)
