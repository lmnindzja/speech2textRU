import io
from unittest.mock import patch, MagicMock
import pytest

@pytest.fixture
def mocked_file_uploader(monkeypatch):
    def mock_file_uploader(*args, **kwargs):
        return io.BytesIO(b"dummy_audio_data")

    monkeypatch.setattr("streamlit.file_uploader", mock_file_uploader)

@pytest.fixture
def mocked_asr_pipeline(monkeypatch):
    def mock_asr_pipeline(*args, **kwargs):
        return MagicMock(return_value="Mocked ASR result")

    monkeypatch.setattr("transformers.pipelines.pipeline", mock_asr_pipeline)

def test_asr_app_with_file(mocked_file_uploader, mocked_asr_pipeline, capsys):
    import 05-model.py  # Подставьте имя вашего файла скрипта
    captured = capsys.readouterr()
    assert "Filename: dummy_audio_data" in captured.out
    assert "Mocked ASR result" in captured.out

def test_asr_app_without_file(capsys):
    import 05-model.py  # Подставьте имя вашего файла скрипта
    captured = capsys.readouterr()
    assert "Upload a file" in captured.out
    assert "Filename:" not in captured.out
