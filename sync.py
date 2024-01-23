import boto3
from boto3.s3.transfer import TransferConfig, TransferManager
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
transfer_manager = TransferManager(s3)

def sync_s3_to_local(bucket_name, s3_path, local_path):
    transfer_manager.sync(bucket_name, s3_path, local_path)

bucket_name = 'watolink-bucket-1'
s3_path = 'test_folder/'
local_path = 'test_upload_data/'
sync_s3_to_local(bucket_name, s3_path, local_path)