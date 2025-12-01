from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

def generate_qa(text):
    text = text.strip()
    if len(text.split()) < 5:
        return "Context too short. Please provide a longer paragraph."
    
    prompt = f"""
Generate ONE English reading comprehension question AND its correct answer 
based ONLY on the context below.

Strict rules:
- The question MUST be directly answerable from the given text.
- The answer MUST be a phrase EXACTLY found in the text.
- DO NOT use outside knowledge.
- If the text does not contain enough information, respond exactly:
  "Question: Not enough information\nAnswer: Not enough information"

Context: \"\"\"{text}\"\"\"

Output format ONLY:
Question: ...
Answer: ...
"""
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to(device)
    
    output = "Question: Not enough information\nAnswer: Not enough information"

    try:
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=250,
                num_beams=5,
                no_repeat_ngram_size=3,
                early_stopping=True
            )
        output = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        if "Answer:" not in output:
            output += "\nAnswer: Not enough information"
    except Exception as e:
        output += f"\n[Error during generation: {e}]"

    return output

if __name__ == "__main__":
    while True:
        context = input("\nNhập đoạn văn (hoặc gõ 'exit' để thoát): ")
        if context.lower() == "exit":
            break
        print("AI Q&A:\n", generate_qa(context))