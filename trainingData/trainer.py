import os
import json
import PyPDF2
import tiktoken

# Función para contar tokens usando tiktoken
def count_tokens(text, model="gpt-3.5-turbo"):
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))

# Función para dividir el texto en fragmentos que no excedan el límite de tokens
def split_text_into_chunks(text, max_tokens=4096):
    enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
    tokens = enc.encode(text)
    chunks = []
    current_chunk = []
    current_tokens = 0

    for token in tokens:
        if current_tokens + 1 > max_tokens:
            chunks.append(enc.decode(current_chunk))
            current_chunk = []
            current_tokens = 0
        current_chunk.append(token)
        current_tokens += 1
    
    if current_chunk:
        chunks.append(enc.decode(current_chunk))
    
    return chunks

# Función para convertir archivos PDF a texto
def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page_text = reader.pages[page_num].extract_text()
            page_text = page_text.replace('\t', ' ')
            text += page_text.replace('\n', ' ')
    return text

# Función principal
def convert_pdfs_to_jsonl(pdf_folder, jsonl_path, max_tokens_per_chunk=4096):
    data = []
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            text = pdf_to_text(pdf_path)
            chunks = split_text_into_chunks(text, max_tokens_per_chunk)
            message_data = {
                "messages": [
                    {"role": "system", "content": "Imagina que eres un Especialista en Evaluación de Propuestas de Proyectos, tu objetivo principal de esta posición es evaluar la capacidad técnica y la experiencia de las empresas que se postulan para proyectos de desarrollo impulsados por el Banco Interamericano de Desarrollo (BID), asegurando que los seleccionados cumplan con los más altos estándares de calidad y experiencia en proyectos similares"},
                ]
            }
            for chunk in chunks:
                message_data["messages"].append({"role": "user", "content": chunk})
                # message_data["messages"].append({"role": "user", "content": ""})


            message_data["messages"].append({"role": "user", "content": "¿Cuál es la experiencia de la empresa en proyectos similares?"})
            message_data["messages"].append({"role": "assistant", "content": "respuesta del modelo 1"})
            message_data["messages"].append({"role": "user", "content": "¿Cuáles son las certificaciones y calificaciones del equipo de trabajo?"})
            message_data["messages"].append({"role": "assistant", "content": "respuesta del modelo 2"})
            message_data["messages"].append({"role": "user", "content": "¿Qué recursos tecnológicos y logísticos tiene la empresa?"})
            message_data["messages"].append({"role": "assistant", "content": "respuesta del modelo 3"})
            message_data["messages"].append({"role": "user", "content": "¿Cómo ha gestionado la empresa los desafíos técnicos en proyectos anteriores?"})
            message_data["messages"].append({"role": "assistant", "content": "respuesta del modelo 4"})
            message_data["messages"].append({"role": "user", "content": "¿Cómo asegura la empresa la calidad en sus proyectos?"})
            message_data["messages"].append({"role": "assistant", "content": "respuesta del modelo 5"})

            message_data["messages"].append({"role": "user", "content": "Teniendo en cuenta las preguntas anteriores ¿Con qué porcentaje de viabilidad ve usted la empresa para calificar a un proceso de desarrollo?"})
            message_data["messages"].append({"role": "assistant", "content": "respuesta del modelo puntaje"})
            data.append(message_data)

    with open(jsonl_path, "w", encoding="utf-8") as jsonl_file:
        for item in data:
            jsonl_file.write(json.dumps(item,ensure_ascii=False) + "\n")

# Uso del script
pdf_folder = "./documents"
jsonl_path = "./fine-tuning.jsonl"
convert_pdfs_to_jsonl(pdf_folder, jsonl_path)
