import streamlit as st
import pandas as pd
import numpy as np


st.title("Dashboard Twitter US Airline Sentiment")
st.write("Sentiment Analysis of Tweets 🕊 about US Airline")

st.sidebar.title("Dashboard")

url = "Dashboard-Twitter_US_Airline_Sentiment/Tweets.csv"

st.chace(persist=True)
def load_data():
  data = pd.read_csv(url)
  data['tweet_created'] = pd.to_datetime(data['tweet_created'])
  return data

