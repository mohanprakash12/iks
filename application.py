import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Select an Option", 
    ["Sentiment Analysis",])

if option == "Sentiment Analysis":
    text = st.text_area(label="Enter text")
    if text: 
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)
