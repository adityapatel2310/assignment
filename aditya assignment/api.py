"""Backend for News Scraping, Sentiment, and TTS"
Handles API calls for news extraction, sentiment analysis, and TTS."""

from flask import Flask, request, jsonify
from utils import fetch_news, analyze_sentiment, generate_hindi_tts

app = Flask(__name__)

@app.route("/get_news", methods=["GET"])
def get_news():
    company = request.args.get("company")
    articles = fetch_news(company)

    if not articles:
        return jsonify({"error": "No articles found"}), 404

    # Sentiment & Comparative Analysis
    for article in articles:
        article["Sentiment"] = analyze_sentiment(article["Summary"])

    # Generate Hindi TTS
    generate_hindi_tts(articles)

    return jsonify({"Company": company, "Articles": articles, "Audio": "output.mp3"})

if __name__ == "__main__":
    app.run(debug=True)