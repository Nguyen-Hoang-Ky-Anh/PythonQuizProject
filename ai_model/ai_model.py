from openai import OpenAI
from dotenv import load_dotenv
import os
import random

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Bạn là một AI học sinh cấp 2 tham gia quiz.
Bạn không được quá giỏi, thỉnh thoảng phải trả lời sai.
Tỉ lệ trả lời đúng chỉ khoảng 60%.
Nếu không chắc chắn thì đoán đại.
Không dùng từ ngữ quá thông minh.
"""

def fake_wrong_answer(correct):
    """Tạo câu trả lời sai cho AI"""
    choices = ["A", "B", "C", "D"]
    wrong_choices = [c for c in choices if c != correct.upper()]

    reasons = [
        "Em đoán vậy thôi ạ.",
        "Không chắc lắm nhưng nghĩ vậy.",
        "Có vẻ là đáp án này...",
        "Em làm đại ạ."
    ]

    return random.choice(wrong_choices) + " - " + random.choice(reasons)


def ask_ai_for_quiz(question: str, correct_answer: str, ai_level=0.6) -> str:
    """
   AI trả lời đúng 60%.
    """
    # Random để AI trả lời sai
    if random.random() > ai_level:
        return fake_wrong_answer(correct_answer)

    # Trả lời đúng (gọi GPT)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ],
            max_tokens=100
        )

        return response.choices[0].message["content"]

    except Exception as e:
        return f"Lỗi khi gọi AI: {e}"
