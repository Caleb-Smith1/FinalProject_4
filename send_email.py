import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

# These values come from the .env file and are hidden from GitHub using .gitignore

def send_newsletter(summaries):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = "📰 Your AI-Powered News Summary"

    # Build the email body
    body = "Here are your summarized news articles:\n\n"
    for i, (title, url, summary) in enumerate(summaries, 1):
        body += f"{i}. {title}\n{url}\nSummary: {summary}\n\n"

    msg.attach(MIMEText(body, 'plain'))
# Connect to gmail using built in smtplib and sends the email. 

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", e)
