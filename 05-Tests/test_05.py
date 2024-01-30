
import io
import streamlit as st
from transformers import pipeline
from unittest.mock import patch

def test_asr_app_with_file():
    # Подготовка моков для ввода/вывода
    input_data = b"dummy_audio_data"
    output_data = "Mocked ASR result"
    
    with patch("streamlit.file_uploader", return_value=io.BytesIO(input_data)):
        with patch("transformers.pipelines.pipeline", return_value=lambda x: output_data):
            with patch("streamlit.write") as mock_write:
                # Имитация выполнения вашего кода
                import model

    # Проверки результатов
    mock_write.assert_called_with("Filename: dummy_audio_data")
    assert "Mocked ASR result" in [call.args[0] for call in mock_write.call_args_list]

