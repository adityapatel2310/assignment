"""Web UI with Streamlit
This script creates a simple UI where users enter a company name, and it displays the results.
"""
import streamlit as st
import requests

st.title(" News Summarization & Sentiment Analysis with Hindi TTS")

company_name = st.text_input("Enter a company name:", "Tesla")

if st.button("Fetch News"):
    response = requests.get(f"http://127.0.0.1:5000/get_news?company={company_name}")
    if response.status_code == 200:
        data = response.json()
        st.write("### News Summary & Sentiment Analysis")
        for article in data["Articles"]:
            st.subheader(article["Title"])
            st.write(f"**Summary:** {article['Summary']}")
            st.write(f"**Sentiment:** {article['Sentiment']}")
            st.write(f"**Topics:** {', '.join(article['Topics'])}")
            st.write("---")

        # Play Hindi TTS
        st.audio("output.mp3", format="audio/mp3")
    else:
        st.error("Failed to fetch news. Try again.")
