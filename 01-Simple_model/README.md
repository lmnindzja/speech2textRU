# Модуль №1. Простое приложение без интерфейсов на основе готовой модели машинного обучения

## Описание
Приложение распознаёт текст из аудио файла на английском языке.
Использована модель whisper-small (содержит  38 млн параматеров) из библиотеки huggingface [whisper-small](https://huggingface.co/openai/whisper-small).

### Использование модели  
        from transformers import pipeline
        audio_link="http://www.moviesoundclips.net/movies1/backtothefuture/style.mp3"
        asr = pipeline("automatic-speech-recognition",   
                              "openai/whisper-small")    
        
        text = asr(audio_link)
        print (text)

