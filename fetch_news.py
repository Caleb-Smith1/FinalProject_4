# Import required libraries and custom modules for fetching, summarizing, and emailing news
import os
import requests
from dotenv import load_dotenv
from summarize import summarize_article
from send_email import send_newsletter

# Load environment variables
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Uses the NewsAPI key to send a request for the top U.S. technology news articles

def fetch_news():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',
        'category': 'technology',
        'pageSize': 5,
        'apiKey': NEWS_API_KEY
    }
# Sends the request to NewsAPI and extracts each article’s title, URL, and content
    
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Failed to fetch news:", response.status_code, response.text)
        return []

    articles = response.json().get('articles', [])
    return [(article['title'], article['url'], article.get('content', '')) for article in articles]

if __name__ == "__main__":
    news_articles = fetch_news()
    summaries = []

# Send each article's content to OpenAI, summarize it, and print the result in the terminal

    for i, (title, url, content) in enumerate(news_articles, 1):
        summary = summarize_article(content)
        summaries.append((title, url, summary))
        print(f"{i}. {title}\n   {url}\n   Summary: {summary}\n")

    # Send the summaries via email
    send_newsletter(summaries)
