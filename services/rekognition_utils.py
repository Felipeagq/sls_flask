import boto3
from botocore.exceptions import ClientError
from . import aws_client
from dotenv import load_dotenv
import os


load_dotenv()
ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")

def obtener_bytes_imagen(ruta_imagen):
    with open(ruta_imagen, "rb") as imagen:
        return imagen.read()

def comparar_rostros_local(cliente,ruta_imagen1,ruta_imagen2):
    bytes_1 = obtener_bytes_imagen(ruta_imagen1)
    bytes_2 = obtener_bytes_imagen(ruta_imagen2)

    
    try:
        respuesta = cliente.compare_faces(SourceImage = {'Bytes' : bytes_1}, 
                                        TargetImage = {'Bytes': bytes_2},
                                        SimilarityThreshold = 60,
                                        QualityFilter = 'NONE'
                                        )


        if respuesta and respuesta.get('ResponseMetadata').get('HTTPStatusCode') == 200:
            # UnmatchedFaces
            for i in respuesta['UnmatchedFaces']:
                print("NO ENCAJA")
                print(i)
                print('\n')
                return {"Match":"No"}

            # FaceMatches
            for i in respuesta['FaceMatches']:
                print("SI ENCAJA")
                # FACE
                print('BoundingBoxWidth: ',i['Face']['BoundingBox']['Width'])
                print('BoundingBoxHeight: ',i['Face']['BoundingBox']['Height'])

                # QUALITY
                print('QualityBrightness: ',i['Face']['Quality']['Brightness'])
                print('QualitySharpness: ',i['Face']['Quality']['Sharpness'])
                
                # SIMILARITY
                print('Similarity: ', i['Similarity'])
                
                return {"Match":"yes",
                        "Similarity":i['Similarity']}


        #QUALITY FILTER: NONE'|'AUTO'|'LOW'|'MEDIUM'|'HIGH'

    except ClientError as error:
        print("Ocurrio un error al llamar a la API:",error)




def comparar_rostros(cliente,bytes_1,bytes_2):

    
    try:
        respuesta = cliente.compare_faces(SourceImage = {'Bytes' : bytes_1}, 
                                        TargetImage = {'Bytes': bytes_2},
                                        SimilarityThreshold = 60,
                                        QualityFilter = 'NONE'
                                        )


        if respuesta and respuesta.get('ResponseMetadata').get('HTTPStatusCode') == 200:
            # UnmatchedFaces
            for i in respuesta['UnmatchedFaces']:
                print("NO ENCAJA")
                print(i)
                print('\n')
                return {"Match":"No"}

            # FaceMatches
            for i in respuesta['FaceMatches']:
                print("SI ENCAJA")
                # FACE
                print('BoundingBoxWidth: ',i['Face']['BoundingBox']['Width'])
                print('BoundingBoxHeight: ',i['Face']['BoundingBox']['Height'])

                # QUALITY
                print('QualityBrightness: ',i['Face']['Quality']['Brightness'])
                print('QualitySharpness: ',i['Face']['Quality']['Sharpness'])
                
                # SIMILARITY
                print('Similarity: ', i['Similarity'])
                
                return {"Match":"yes",
                        "Similarity":i['Similarity']}


        #QUALITY FILTER: NONE'|'AUTO'|'LOW'|'MEDIUM'|'HIGH'

    except ClientError as error:
        print("Ocurrio un error al llamar a la API:",error)






if __name__ == "__main__":
    cliente = aws_client.client_aws(ACCESS_KEY_ID,SECRET_ACCESS_KEY,"rekognition")
    rose_my_baby_1 = "rose_1.jpg"
    rose_my_baby_2 = "rose_2.jpg"
    comparar_rostros_local(cliente,rose_my_baby_1,rose_my_baby_2)
    
    print("*"*100)
    
    rose_my_baby_1 = "rose_1.jpg"
    jennie_my_baby_2 = "jennie.jpg"
    comparar_rostros(cliente,rose_my_baby_1,jennie_my_baby_2)