from flask import Flask, request, jsonify
from flask_cors import CORS
import azureConnection  # Importa tu archivo de Python que maneja la conexión a Azure OpenAI

app = Flask(__name__)
CORS(app)

@app.route('/api/companySummary', methods=['POST'])
def consulta():
    data = request.json
    companyName = data.get('companyName')

    # Aquí llamas a la función de tu archivo Python que se conecta a Azure OpenAI
    response = azureConnection.azureRequest(companyName)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
