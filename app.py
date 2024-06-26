import streamlit as st
from transformers import pipeline
import requests

asr = pipeline("automatic-speech-recognition", "lorenzoncina/whisper-small-ru", chunk_length_s=30)


def asr_app_from_audio_file(audio_file_path):
    st.write("Processing audio from file: ", audio_file_path)

    try:
        audio_response = requests.get(audio_file_path)
        audio_response.raise_for_status()  # Проверка наличия ошибок при получении звука
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching audio from file: {e}")
        return

    file_to_model = audio_response.content

    text = asr(file_to_model, batch_size=8)
    st.write(text)
# ASR from URL f.e http://www.moviesoundclips.net/movies1/backtothefuture/style.mp3


uploaded_file = st.text_input("Enter audio file URL")
if st.button("Process Audio"):
    asr_app_from_audio_file(uploaded_file)

# ASR from file dropbox
uploaded_file = st.file_uploader("Upload a audio file")

if uploaded_file:
    st.write("Filename: ", uploaded_file.name)
    file_to_model = uploaded_file.getvalue()

    text = asr(file_to_model, batch_size=8)
    st.write(text)
