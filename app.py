# Librerias de terceros
from dotenv import load_dotenv
import os
from flask import Flask

# Librerias propias
from services.s3_utils import create_presigned_url, post_image_s3
from services.aws_client import client_aws
from services.utils import response_func
from services.utils import Config

load_dotenv()
ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")

app = Flask(__name__)
app.config.from_object(Config)

@app.errorhandler(404)
def resource_not_found(e):
    return response_func(
        "Page Not Found",
        404,
        None
    )


@app.route("/")
def hello_check():
    return response_func(
        "ok",
        200,
        "Hello World"
    )

from routes.generate_links_route import generate_link_bp
app.register_blueprint(generate_link_bp)

from routes.rekognition_route import rekognition_bp
app.register_blueprint(rekognition_bp)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000,
        host="0.0.0.0"
    )





