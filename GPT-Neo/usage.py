def ask_question(model, tokenizer, question, context):
    input_text = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(inputs.input_ids, max_length=2000)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer