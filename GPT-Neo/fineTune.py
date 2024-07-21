from transformers import GPTNeoForCausalLM, GPT2Tokenizer, Trainer, TrainingArguments, AutoTokenizer, DataCollatorForLanguageModeling
from datasets import Dataset

def prepare_dataset(pdf_texts):
    data = [{"text": text} for title, text in pdf_texts.items()]
    return Dataset.from_dict({"text": data})

def fine_tune_model(pdf_texts, model_name='EleutherAI/gpt-neo-125M'):
    # Prepara el dataset
    dataset = prepare_dataset(pdf_texts)

    print(dataset)

    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        
    # Tokenización
    def tokenize_batch(batch):
        inputs = tokenizer(batch['text'][0]['text'], truncation=True, padding="max_length", max_length=12)
        
        return inputs

    tokenized_datasets = dataset.map(tokenize_batch, batched=True)

    model = GPTNeoForCausalLM.from_pretrained(model_name)
    
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )


    training_args = TrainingArguments(
        output_dir='./results',
        per_device_train_batch_size=1,
        num_train_epochs=1,
        logging_dir='./logs',
        logging_steps=10,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=tokenized_datasets,
    )

    trainer.train()

    return model, tokenizer
