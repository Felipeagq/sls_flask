from distutils.debug import DEBUG
import os
from services.aws_client import client_aws
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    DEBUG:bool = True
    ACCESS_KEY_ID:str = os.getenv("ACCESS_KEY_ID")
    SECRET_ACCESS_KEY:str = os.getenv("SECRET_ACCESS_KEY")
    BUCKET_NAME:str = os.getenv("BUCKET_NAME")
    FOLDER:str = os.getenv("FOLDER")
    FLASK_APP:str ="app.py"

    CLIENTE_S3 = client_aws(ACCESS_KEY_ID,SECRET_ACCESS_KEY,"s3")
    CLIENTE_REKOGNITION = client_aws(ACCESS_KEY_ID,SECRET_ACCESS_KEY,"rekognition")

def response_func(msg,status,data):
    return {
        "msg":msg,
        "status":status,
        "data":data
        }