from pdfExtractor import extract_texts_from_pdfs
from fineTune import fine_tune_model
from usage import ask_question

def main():
    folder_path = '../trainingData/documents/'
    pdf_texts = extract_texts_from_pdfs(folder_path)
    model, tokenizer = fine_tune_model(pdf_texts)
    for filename, context in pdf_texts.items():
        question = "¿Cuál es el tema principal de este documento?"
        answer = ask_question(model, tokenizer, question, filename)
        print(f"PDF: {filename}")
        print(f"Pregunta: {question}")
        print(f"Respuesta: {answer}")
        print("="*50)

if __name__ == "__main__":
    main()
