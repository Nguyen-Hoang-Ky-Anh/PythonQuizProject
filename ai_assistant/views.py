from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key từ .env
load_dotenv()

# Tạo client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(question: str) -> str:
    """Gửi câu hỏi đến GPT-4o mini và nhận câu trả lời."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Bạn là AI trả lời câu hỏi ngắn gọn, rõ ràng và chính xác."
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            max_tokens=250
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Lỗi khi gọi AI: {e}"

