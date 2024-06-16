# PruebaTecnicaChallenge

Repositorio para la prueba técnica de Azure con Azure Function, incluyendo la extracción de datos de Kaggle y almacenamiento en ADLS, y posteriormente insertar en una BD SQL Server para posteriormente hacer un reporte conectándose a la tabla.

## Descripción

Este proyecto tiene como objetivo:

1. **Extracción de datos**: Utilizando Azure Functions para descargar un dataset desde Kaggle.
2. **Almacenamiento de datos**: Guardar el dataset en Azure Data Lake Storage (ADLS).
3. **Inserción de datos en SQL Server**: Insertar los datos del dataset en una base de datos SQL Server.
4. **Generación de reportes**: Crear reportes a partir de los datos almacenados en SQL Server.

## Estructura del proyecto

- **Azure Functions**: Contiene el código para la función que extrae y almacena datos.
- **Data Lake Storage**: Configuración y almacenamiento de los datos en ADLS.
- **SQL Server**: Scripts y configuraciones para la base de datos SQL Server.

## Instalación

1. Clonar el repositorio:
    ```sh
    git clone https://github.com/malmeydar/PruebaTecnicaChallenge.git
    cd PruebaTecnicaChallenge
    ```

2. Configurar el entorno virtual de Python:
    ```sh
    python -m venv EnviromentFunction
    source EnviromentFunction/Scripts/activate  # En Windows
    # source EnviromentFunction/bin/activate  # En Mac/Linux
    ```

3. Instalar las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Configuración

1. Crear un archivo `local.settings.json` con las siguientes variables:
    ```json
    {
        "IsEncrypted": false,
        "Values": {
            "AzureWebJobsStorage": "<Your Azure Storage Connection String>",
            "FUNCTIONS_WORKER_RUNTIME": "python",
            "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
            "KAGGLE_URL": "https://www.kaggle.com/datasets/anoopjohny/consumer-complaint-database/download",
            "ADLS_CONNECTION_STRING": "<Your ADLS Connection String>",
            "CONTAINER_NAME": "kaggle"
        }
    }
    ```

## Uso

Para ejecutar la función localmente:
```sh
func start
