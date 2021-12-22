# Importing the Necessary Libraries
import streamlit as st  # The Streamlit Library is used to setup the app
import yfinance as yf  # The YahooFinance is used to get the realtime stock charts
from Googlnews import newsgoogle as ng  # The file is used to scrape the news headlines using selenium
from SentimentAnalyzer import stocksentiment as ss  # The file is used to analyze the sentiment of the stocks using nltk
from datetime import datetime  # Used to import the datetime

# Creating the Streamlit App
st.title("Real Time Stock Sentiment Analyzer")
search_key = st.text_input("Enter a Stock Name", placeholder="ex: HDFC", value="").upper()  # Getting the search value

if st.button("Search"):
    ng(search_key)
    result = ss("news.csv")

    if result == "Positive":
        Comment = "Which Means Got to Buy Some Stocks!"
    elif result == "Negative":
        Comment = "Which Means Got to Sell Some Stocks!"
    else:
        Comment = "Which Means Got to Wait for a bit..."

    st.subheader("The Analyzer Shows that the " + search_key + " Stock is " + result)
    st.subheader(Comment)

    score = round(ss.score, 3)
    st.text("The Sentiment score is " + str(score))

    # Getting the Stock chart from yahoo finance
    end_date = datetime.now()
    stock = search_key + ".NS"
    stockdata = yf.Ticker(stock)
    tickerDf = stockdata.history(period='1d', start='2021-11-01', end=end_date)
    st.line_chart(tickerDf.Close)
    st.bar_chart(tickerDf.Volume)
    
    
    st.write("Made by: Ramesh Kumar")
