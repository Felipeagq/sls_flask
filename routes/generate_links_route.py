from services.s3_utils import create_presigned_url,post_image_s3
from flask import Blueprint, request
from dotenv import load_dotenv
import os 
from services.utils import response_func ,Config

load_dotenv()

BUCKET_NAME = os.getenv("BUCKET_NAME")
FOLDER = os.getenv("FOLDER")


# Creación del BluePrint
generate_link_bp = Blueprint(
    "generate_link_bp",
    __name__,
    url_prefix="/api/v1/"
)

# Creación de la ruta
@generate_link_bp.route(
    "/generate/links",
    methods=["POST"]
)
def generate_links():
    # Identificar el Verbo HTTPs
    if request.method == "POST":
        
        # Adquisición de la data del JSON
        quantity = request.get_json().get("quantity",1)
        names = request.get_json().get("names",None)
        id_client = request.get_json().get("id_client",None)
        
        # Validación de la data del JSON
        if not names or not id_client:
            return response_func(
                "debe haber nombres y el id_cliente",
                400,
                None
            )
        
        # Validador, cantidad de links y cantidad de nombres
        if quantity != len(names):
            return response_func(
                "error, cantidad y numero de nombres no es igual",
                400,
                None
            )
            
        # Generación de los Links
        try:
            links = []
            for i in range(quantity):
                response = create_presigned_url(
                    Config.CLIENTE_S3,
                    Config.BUCKET_NAME,
                    f"{Config.FOLDER}/{id_client}/{names[i]}.jpg"
                )
                links.append(response)
            
            
            ## Prueba de subir archivos
            # file = {"file":open("cc_back.jpeg","rb")}
            # r = post_image_s3(
            #     response=links[1],
            #     file=file
            # )
            # file = {"file":open("cc_front.jpeg","rb")}
            # r = post_image_s3(
            #     response=links[0],
            #     file=file
            # )
            
            
            # file = {"file":open("felipe_cara.jpeg","rb")}
            # r = post_image_s3(
            #     response=links[0],
            #     file=file
            # )
            
            # retorno de los links
            return response_func(
                "ok",
                200,
                    {
                    "links":links
                }
            )
        # Captura de algún error al momento de generar los Links
        except Exception as e:
            print(e)
            return response_func(
                e,
                400,
                None
            )