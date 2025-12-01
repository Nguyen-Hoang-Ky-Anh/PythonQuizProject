from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_name = "Helsinki-NLP/opus-mt-vi-en"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

def translate_vi_to_en(sentence):
    inputs = tokenizer(sentence, return_tensors="pt").to(device)
    
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=200)
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    while True:
        q = input("\nNhập câu tiếng Việt (hoặc gõ 'exit' để thoát): ")
        if q.lower() == "exit":
            break
        print("AI dịch:", translate_vi_to_en(q))