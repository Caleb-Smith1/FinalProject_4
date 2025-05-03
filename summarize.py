import os
import openai
from dotenv import load_dotenv

# Load your OpenAI API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_article(text):
    if not text or len(text.strip()) < 20:
        return "Not enough content to summarize."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes news articles into 1-2 sentences."},
                {"role": "user", "content": f"Summarize this article:\n\n{text}"}
            ],
            max_tokens=100
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"
