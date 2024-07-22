# def ask_question(model, tokenizer, question, context):
#     input_text = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
#     inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
#     outputs = model.generate(
#         inputs["input_ids"],
#         attention_mask=inputs["attention_mask"],
#         max_length=2048,
#         num_return_sequences=1,
#         pad_token_id=tokenizer.eos_token_id
#     )
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     print ("RESPUESTA-----------------------------------------------------------------")
#     # print (response)
    
#     return response.split("Answer:")[1].strip()


def split_text(text, tokenizer, max_length=1800):
    """Divide el texto en fragmentos manejables."""
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        if len(tokenizer.encode(' '.join(current_chunk + [word]))) < max_length:
            current_chunk.append(word)
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

def generate_responses_for_chunks(model, tokenizer, chunks, question, max_length=2048):
    responses = []
    
    for chunk in chunks:
        input_text = f"Context: {chunk}\n\nQuestion: {question}\n\nAnswer:"
        inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
        
        outputs = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=max_length+1,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id
        )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # print(response)
        response = response.split("Answer:")[1].strip()
        responses.append(response)
    
    return responses

def combine_responses(responses):
    """Combina las respuestas de los fragmentos en una respuesta final."""
    return ' '.join(responses)
