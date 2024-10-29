import io
import os
import boto3

R2_ACCESS_KEY_ID = os.environ["R2_ACCESS_KEY_ID"]
R2_SECRET_ACCESS_KEY = os.environ["R2_SECRET_ACCESS_KEY"]
R2_S3_ENDPOINT_URL = os.environ["R2_S3_ENDPOINT_URL"]
R2_DOMAIN_NAME = os.environ["R2_DOMAIN_NAME"]

s3 = boto3.client(
    service_name ="s3",
    endpoint_url = R2_S3_ENDPOINT_URL,
    aws_access_key_id = R2_ACCESS_KEY_ID,
    aws_secret_access_key = R2_SECRET_ACCESS_KEY,
    region_name="auto", # Must be one of: wnam, enam, weur, eeur, apac, auto
)

def upload_to_r2(bucket_name, arxiv_id, filename):
    obj_name = os.path.join(arxiv_id, os.path.basename(filename))

    with open(filename, 'rb') as f:
        file_content = f.read()

    s3.upload_fileobj(io.BytesIO(file_content), bucket_name, obj_name)
    return f"https://{R2_DOMAIN_NAME}/{obj_name}"

def remove_r2_directory(bucket_name, arxiv_id):
    s3.delete_object(Bucket=bucket_name, Key=arxiv_id)