import pytest
from model import asr_app_from_audio_file

def test_asr_app_with_real_audio_file(capsys):
    audio_url = "http://www.moviesoundclips.net/movies1/backtothefuture/style.mp3"
    
    # Вызываем функцию и захватываем вывод
    with capsys.disabled():
        asr_app_from_audio_file(audio_url)
