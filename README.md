# 📰 AI-Powered News Newsletter Generator

This project is a Python-based automation tool that fetches the latest technology news, summarizes each article using OpenAI’s GPT model, and emails a clean, concise news digest daily. It is designed to keep users informed with minimal time investment.

---

## ✨ Features

- Retrieves top headlines from NewsAPI  
- Summarizes articles using OpenAI’s GPT (v1+)  
- Sends a well-formatted email digest using Gmail  
- Automatically runs daily via Windows Task Scheduler  
- Uses a `.env` file to securely store API keys and credentials  

---

## 🔧 How It Works

### 1. **Fetching News**
Uses NewsAPI to retrieve the top 5 U.S. technology headlines.

### 2. **Summarizing Articles**
Each article’s content is summarized using OpenAI's GPT-3.5, reduced to 1–2 concise sentences.

### 3. **Email Formatting and Delivery**
Summaries are formatted and emailed using Python’s built-in `smtplib`.

### 4. **Automation**
The process is scheduled to run daily using Windows Task Scheduler.

---

## 📁 File Overview

| File             | Purpose                                        |
|------------------|------------------------------------------------|
| `fetch_news.py`  | Main script: fetches, summarizes, and emails news |
| `summarize.py`   | Summarizes article content using OpenAI API    |
| `send_email.py`  | Formats and sends the email using `smtplib`    |
| `.env`           | Stores sensitive credentials (ignored by Git)  |
| `requirements.txt` | Lists required Python packages                |
| `README.md`      | Project overview and instructions              |

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt

# Setup your env files

NEWS_API_KEY=your_newsapi_key_here
OPENAI_API_KEY=your_openai_key_here
EMAIL_ADDRESS=your_gmail_address_here
EMAIL_PASSWORD=your_gmail_app_password_here
RECEIVER_EMAIL=your_recipient_email_here

#How to Run
python fetch_news.py
