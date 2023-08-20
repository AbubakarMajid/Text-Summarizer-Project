import streamlit as st
from TextSummarizer.pipeline.prediction import PredictionPipeline



text = st.chat_input("Enter any Text here")


pipeline = PredictionPipeline()
prediction = pipeline.predict(text)


with st.chat_message("User"):
    st.write(text)

with st.chat_message("assistant"):
    st.write(prediction)