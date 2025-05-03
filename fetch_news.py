import os
import requests
from dotenv import load_dotenv
from summarize import summarize_article  # Make sure summarize.py is in the same folder

# Load environment variables from .env file
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',
        'category': 'technology',
        'pageSize': 5,
        'apiKey': NEWS_API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Failed to fetch news:", response.status_code, response.text)
        return []

    articles = response.json().get('articles', [])
    return [(article['title'], article['url'], article.get('content', '')) for article in articles]

# Run the script
if __name__ == "__main__":
    news_articles = fetch_news()

    for i, (title, url, content) in enumerate(news_articles, 1):
        print(f"{i}. {title}\n   {url}")
        summary = summarize_article(content)  # Only works if OpenAI key is set
        print(f"   Summary: {summary}\n")
