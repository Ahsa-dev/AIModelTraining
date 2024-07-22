from pdfExtractor import extract_texts_from_pdfs
from fineTune import fine_tune_model
from usage import split_text, generate_responses_for_chunks, combine_responses

def main():
    folder_path = '../trainingData/documents/'
    pdf_texts = extract_texts_from_pdfs(folder_path)
    fine_tune_model(pdf_texts)
    # model, tokenizer = 
    # for filename, context in pdf_texts.items():
    #     question = "En una oración corta que no supere las 4 lineas de texto ¿Me puedes decir, en qué manifiesta interés la empresa dentro del documento?"


    #     max_length = 2048  # Longitud máxima en tokens
    #     chunks = split_text(context, tokenizer)
    #     responses = generate_responses_for_chunks(model, tokenizer, chunks, question, max_length)

    #     final_response = combine_responses(responses)


    #     # answer = ask_question(model, tokenizer, question, context)
    #     print(f"PDF: {filename}")
    #     print(f"Pregunta: {question}")
    #     print(f"Respuesta: {final_response}")
    #     print("="*50)

if __name__ == "__main__":
    main()