En este proyecto se encuentra lo siguiente:
- Dentro de la carpeta trainingData, archivos en python que se encargan de recibir los documentos y estructurarlos en un formato JSONL para usar el archivo base de entrenamiento que será enviado a la herramienta Fine-Tuning de OpenAI
- Dentro de la carpeta GPT-Neo, estará una implementación en python que se encarga de recibir los documentos, procesarlos, crear un modelo a partir de GPT-Neo y guardarlo en la carpeta results. Además de haber una implementación donde se carga un documento y se le realizan preguntas al respecto.
- Dentro de la carpeta documents, se encontrarán todos los documentos que se usarán para entrenar al modelo, nuevamente estos archivos estarán dentro del git ignore ya que es información que no es necesaria compartir
- Dentro de la carpeta de credentials, se encontará un archivo de credenciales con la configuración para la conexión con azureOpenAI, archivo que por obvias razones no está en el repositorio pero tiene una estructura similar a
```bash

DEPLOYMENT_NAME = "nombre de la implementación de ai.azure"
ENDPOINT_URL = "https://tu-punto-de-conexión.openai.azure.com/"
SEARCH_KEY = "key del search service de azure"
SEARCH_ENDPOINT = "https://nombre-de-tu-search-service.search.windows.net"
SEARCH_INDEX = "nombre del índice creado dentro de tu search service"
```

# Implementación de azureOpenAI

Para hacer una implementación debes correr tanto el backend como el frontend.\

### backend

Dentro de la carpeta azureOpenAI/backend encontrarás el archivo de conexión con azure y un archivo API que contiene una aplicación flask.\
Desde la misma carpeta backend simplemente ejecutas el archivo API `py API.py` y ya deberías tener corriendo el backend por defecto en [http://localhost:5000](http://localhost:5000)

### frontend

Dentro de la carpeta azureOpenAI/frontend encontrarás un proyecto pequeño de react que no tiene mucha complicación entenderlo.\
Para iniciarlo sólo debes correr `npm install` y posteriromente `npm start`.

**Nota: Las versiones utilizadas en el proyecto son para node v20.17.0 y para python 3.12.4**