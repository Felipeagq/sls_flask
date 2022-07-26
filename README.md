# Serverless
## Paso a paso del deploy
- Creo una capa, montando una .zip.
- lo monto a AWS Lambda layers
- Creo un ````npm -i serverless````
- ````npm i serverless-wsgi````
- instalo el wsgi de flask: ````npx sls plugin install --name severless-wsgi````
- instalo el wsgi de flask: ````npx sls plugin install --name severless-python-requirements````
- Copiar los archivos ````wsgi_handler.py```` y ````serverless_wsgi.py````.
- Tener configurado el ````aws configure```` con la cuenta en default.
- despliego el servidor ````npx sls deploy````.

## Configurar yml
- ````service```` : nombre del servicio.
- ````app```` : ````archivo:entidad```` que quiero correr
- ````layers````: el ***arn*** de la capa creada en ***AWS Lambda Layers***