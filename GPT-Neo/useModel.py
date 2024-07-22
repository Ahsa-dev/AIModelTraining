from pdfExtractor import extract_texts_from_pdfs
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
from usage import split_text, generate_responses_for_chunks, combine_responses


def main():
    model_name = './results'
    folder_path = '../trainingData/documents/'
    pdf_texts = extract_texts_from_pdfs(folder_path)
    
    model, tokenizer = load_model_and_tokenizer(model_name,model_name)

    for filename, context in pdf_texts.items():
        question = "En una oración corta que no supere las 4 lineas de texto ¿Me puedes decir, en qué manifiesta interés la empresa dentro del documento?"

        max_length = 2048  # Longitud máxima en tokens
        chunks = split_text(context, tokenizer)
        responses = generate_responses_for_chunks(model, tokenizer, chunks, question, max_length)

        final_response = combine_responses(responses)


        # answer = ask_question(model, tokenizer, question, context)
        print(f"PDF: {filename}")
        print(f"Pregunta: {question}")
        print(f"Respuesta: {final_response}")
        print("="*50)

def load_model_and_tokenizer(model_path, tokenizer_path):
    """Carga el modelo y el tokenizador desde las rutas especificadas."""
    tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)
    model = GPTNeoForCausalLM.from_pretrained(model_path)
    
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    
    return model, tokenizer

if __name__ == "__main__":
    main()