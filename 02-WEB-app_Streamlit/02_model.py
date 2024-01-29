import io

import streamlit as st
from transformers import pipeline
import numpy as np

asr = pipeline("automatic-speech-recognition", "openai/whisper-small")

uploaded_file = st.file_uploader("Upload a file")

if uploaded_file:
    st.write("Filename: ", uploaded_file.name)
    file_to_model = uploaded_file.getvalue()

    text = asr(file_to_model)
    st.write(text)
