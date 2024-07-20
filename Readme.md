En este proyecto se encuentra lo siguiente:
- Dentro de la carpeta trainingData, archivos en python que se encargan de recibir los documentos y estructurarlos en un formato JSONL para usar el archivo base de entrenamiento que será enviado a la herramienta Fine-Tuning de OpenAI
- Dentro de la carpeta modelUsage, estará una implementación en python que se encarga de recibir el documento, procesarlo y enviarlo al modelo ya entrenado de Fine-Tuning, y realizar una serie de preguntas establecidas para que el modelo puntúe si el documento cumple o no con los estándares requeridos.
- Dentro de la carpeta credentials, estará un archivo JSON (que estará en el git ignore) que cuenta con las credenciales de conexión necesarias para el uso del modelo. Para futuros usos se deberá usar una estructura similar a: 
    {
        TODO: definir estructura
    }
- Dentro de la carpeta documents, se encontrarán todos los documentos que se usarán para entrenar al modelo, nuevamente estos archivos estarán dentro del git ignore ya que es información que no es necesaria compartir