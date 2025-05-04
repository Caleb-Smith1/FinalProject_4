import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Create OpenAI client using API key from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Sends article content to OpenAI and returns a short summary that will be sent through email

def summarize_article(text):
    if not text or len(text.strip()) < 20:
        return "Not enough content to summarize."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes news articles in 1-2 sentences."},
                {"role": "user", "content": f"Summarize this article:\n\n{text}"}
            ],
            max_tokens=100
        )

        # Returns the summary from OpenAI, or an error message if the request fails
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"
