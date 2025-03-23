"""Helper Functions
This file contains:
News scraping (BeautifulSoup)
Sentiment analysis
Hindi TTS generation"""

import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from gtts import gTTS

def fetch_news(company):
    """Scrapes news articles for a given company name."""
    url = f"https://news.google.com/search?q={company}&hl=en"
    response = requests.get(url)
    
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []
    
    for item in soup.find_all("div", class_="xrnccd")[:10]:  # Limit to 10 articles
        title = item.find("h3").text
        link = item.find("a")["href"]
        summary = item.find("span").text if item.find("span") else "No summary available"

        articles.append({"Title": title, "Summary": summary, "Link": "https://news.google.com" + link})

    return articles

def analyze_sentiment(text):
    """Performs sentiment analysis and classifies as Positive, Negative, or Neutral."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def generate_hindi_tts(articles):
    """Converts summary and sentiment analysis into Hindi speech."""
    text_summary = "\n".join([f"{a['Title']} - {a['Sentiment']}" for a in articles])
    tts = gTTS(text=text_summary, lang="hi")
    tts.save("output.mp3")