import boto3
import os
from botocore.config import Config
from botocore.exceptions import ClientError
import logging
import requests

def client_aws(ACCESS_KEY_ID,SECRET_ACCESS_KEY,service):
    client_aws = boto3.client(service, config=Config(signature_version="s3v4"),
                            region_name="us-east-2",
                            aws_access_key_id=ACCESS_KEY_ID,
                            aws_secret_access_key=SECRET_ACCESS_KEY
                            )
    return client_aws