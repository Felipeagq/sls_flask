from services.s3_utils import create_presigned_url,post_image_s3
from flask import Blueprint, request
from dotenv import load_dotenv
import os 
from services.utils import response_func ,Config
from services.rekognition_utils import comparar_rostros

rekognition_bp = Blueprint(
    "rekognition",
    __name__,
    url_prefix="/api/v1"
)

@rekognition_bp.route(
    "/rekognition",
    methods=["POST"]
)
def rekognition():
    # Identificar el HTTPs
    if request.method == "POST":
        id_client = request.get_json().get("id_client",None)

        # Validación de la data del JSON
        if  not id_client:
            return response_func(
                "El id_cliente debe existir",
                400,
                None
            )
        try:
            # Leer el archivo en binario.
            response = Config.CLIENTE_S3.get_object(
            Bucket = "neero-archivos",
            Key=f"OnBoarding/{id_client}/cc_front.jpg"
            )
            cc_front = response.get("Body").read()
            print(response)
            
            response = Config.CLIENTE_S3.get_object(
            Bucket = "neero-archivos",
            Key=f"OnBoarding/{id_client}/cara.jpg"
            )
            cara = response.get("Body").read()
            print(response)
        except Exception as e:
            print(e)
        
        comparación = comparar_rostros(
            Config.CLIENTE_REKOGNITION,
            cc_front,
            cara
        )
        return response_func(
            "Persona encaja",
            200,
            comparación
        )
        