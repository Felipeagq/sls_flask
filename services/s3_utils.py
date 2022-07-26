import boto3
import os
from botocore.config import Config
from botocore.exceptions import ClientError
import logging
import requests




def create_presigned_url(client, bucket_name, object_name,fields=None, conditions=None, expiration=120):
    """Genera un presigned URL para subir un archivo a S3.
    -----------
    PARAMETROS:
    -----------
    - bucket_name   : (string) nombre del bucket.
    - object_name   : (string) nombre del archivo que se va a subir al S3.
    - expiration    : Tiempo en segundo para que el  presigned URL sea valido.
    - return        : Presigned URL como string. si hay error, returns None.
    """


    # Genera el link presigned URL
    try:
        response = client.generate_presigned_post(Bucket=bucket_name,
                                                    Key=object_name,
                                                    Fields=fields,
                                                    Conditions=conditions,
                                                    ExpiresIn=expiration
                                                    )
    except ClientError as e:
        logging.error(e)
        return None
    # Contiene el presigned URL
    return response


def post_image_s3(response,file):
    try:
        r = requests.post(
            url= response["url"],
            data= response["fields"],   
            files=file
        )
        print(r)
        return r
    except Exception as e:
        print(e)
        return e


