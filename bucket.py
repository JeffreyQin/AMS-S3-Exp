import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

# list all buckets
def list_buckets():
    buckets = s3.list_buckets()['Buckets']
    print(buckets)

# create new bucket
def create_bucket(bucket_name, region="us-east-2"):
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': region}
    )

create_bucket('watolink-bucket-2')