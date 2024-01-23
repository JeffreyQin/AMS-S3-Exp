import os
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def upload_file(local_path, bucket_name, s3_path):
    try:
        s3.upload_file(local_path, bucket_name, s3_path)
        print('upload success')
    except ClientError:
        print('upload error')

local_path = 'local_test_folder/test.csv'
bucket_name = 'watolink-bucket-1'
s3_path = 'test_folder/test2'
upload_file(local_path, bucket_name, s3_path)

"""
def download_file(bucket_name, s3_path, local_path):
    try:
        s3.download_file(bucket_name, s3_path, local_path)
        print('download success')
    except ClientError:
        print('download error')
    
bucket_name = 'watolink-bucket-1'
s3_path = "test_folder/test.csv"
local_path = "test_upload_data/testDownload.csv"
download_file(bucket_name, s3_path, local_path)



def delete_file(bucket_name, s3_path):
    try:
        s3.delete_object(Bucket=bucket_name, Key=s3_path)
        print('delete success')
    except ClientError:
        print('delete error')


    
bucket_name = 'watolink-bucket-1'
s3_path = 'test_folder/dasds'
delete_file(bucket_name, s3_path)
"""



