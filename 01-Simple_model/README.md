## УРФУ 2024. Программная инженерия. Репозиторий команды π-24

# Модуль №1
Приложение распознаёт текст из аудио файла на английском языке.
Использована модель whisper-small (содержит  38 млн параматеров) из библиотеки huggingfac [whisper-small](https://huggingface.co/openai/whisper-small)

### Использование модели  
    from transformers import pipeline
    !wget -O uploaded.mp3 http://www.moviesoundclips.net/movies1/backtothefuture/style.mp3
    asr = pipeline("automatic-speech-recognition",   
                      "openai/whisper-small")


    text = asr('uploaded.mp3')
    print (text)

