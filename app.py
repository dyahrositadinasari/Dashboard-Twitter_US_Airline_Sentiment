import streamlit as st
import pandas as pd
import numpy as np


st.title("Dashboard Twitter US Airline Sentiment")
st.write("Sentiment Analysis of Tweets 🕊 about US Airline")

url = "Dashboard-Twitter_US_Airline_Sentiment/Tweets.csv"

st.cache_data(persist=True)
def load_data():
  data = pd.read_csv(url)
  data['tweet_created'] = pd.to_datetime(data['tweet_created'])
  return data

data = load_data()
st.sidebar.subheader("Show random Tweet")
random_tweet = st.sidebar.radio('Sentiment', ('positive', 'neutral', 'negative'))
st.sidebar.markdown(data.query('airline_sentiment == @random_tweet')[['text']].sample(n=1).iat[0,0])
