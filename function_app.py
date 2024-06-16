import logging
import requests
from azure.storage.blob import BlobServiceClient
import azure.functions as func
import os

# Obteniendo cada de conexion 
CONNECTION_STRING = os.getenv('CONNECTION_STRING')
if CONNECTION_STRING is None:
    raise ValueError("CONNECTION_STRING is not set in the environment variables")

CONTAINER_NAME = "kaggle"  # Nombre del contenedor
if CONTAINER_NAME is None: # Validación nombre del contenedor
    raise ValueError("CONTAINER_NAME is not set")

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)   #Aca se considera ANONYMOUS porque inicialmente se configuro asi

@app.route(route="GetDataFromKaggleNew") #Decorador para acceder al metodo 
def GetDataFromKaggleNew(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.') #Log de procesamiento de solicitud

    # URL del dataset de Kaggle
    url = 'https://www.kaggle.com/datasets/anoopjohny/consumer-complaint-database/download' 

    try:
        # Solicitud HTTP GET al URL de Kaggle
        response = requests.get(url)
        response.raise_for_status()  # Excepción para errores HTTP 
        data = response.content  # Obteniendo el contenido de la respuesta

        if not data:
            raise ValueError("No data retrieved from the URL")

        # Guardando los datos en Azure Data Lake Storage - kaggle
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob="consumer-complaint-database.csv")
        
        blob_client.upload_blob(data, overwrite=True)
        return func.HttpResponse("Data fetched and uploaded successfully", status_code=200)
    
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")       # Error al obtener los datos 
        return func.HttpResponse(f"Error fetching data: {e}", status_code=500)
    except Exception as e:
        logging.error(f"Error uploading data: {e}")      # Error al cargar los datos
        return func.HttpResponse(f"Error uploading data: {e}", status_code=500)
