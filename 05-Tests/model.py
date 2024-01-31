import io
import streamlit as st
from transformers import pipeline
import requests
import ffmpeg

asr = pipeline("automatic-speech-recognition", "openai/whisper-small")

def asr_app_from_audio_file(audio_file_path):
    st.write("Processing audio from file: ", audio_file_path)

    try:
        audio_response = requests.get(audio_file_path)
        audio_response.raise_for_status()  # Проверка наличия ошибок при получении звука
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching audio from file: {e}")
        return

    file_to_model = audio_response.content

    text = asr(file_to_model)
    st.write(text)

# Пример использования в Streamlit
uploaded_file = st.text_input("Enter audio file URL")
if st.button("Process Audio"):
    asr_app_from_audio_file(uploaded_file)

