## УРФУ 2024. Программная инженерия. Репозиторий команды π-24

# Итоговый проект. speech2textRU
speech2textRU - Приложение для конвертации аудио записей на русском языке в текст на основе модели 
[wav2vec2-large-xlsr-53-russian](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-russian)

### Зависимости
    $ pip install huggingsound

### Использование модели  
    from huggingsound import SpeechRecognitionModel
  
    model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-russian")
    audio_paths = ["/path/to/file.mp3", "/path/to/another_file.wav"]
    
    transcriptions = model.transcribe(audio_paths)

### Оценка точности конвертации
    from huggingsound import SpeechRecognitionModel
    
    model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-english")
    
    references = [
        {"path": "/path/to/sagan.mp3", "transcription": "extraordinary claims require extraordinary evidence"},
        {"path": "/path/to/asimov.wav", "transcription": "violence is the last refuge of the incompetent"},
    ]
    
    evaluation = model.evaluate(references)
    
    print(evaluation)
    
    # evaluation format: {"wer": 0.08, "cer": 0.02}
