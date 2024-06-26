from transformers import pipeline
from fastapi import FastAPI, File, UploadFile

asr = pipeline("automatic-speech-recognition", "lorenzoncina/whisper-small-ru")

# Создание экземпляра FastAPI
app = FastAPI()

# Endpoint для проверки доступности сервиса
@app.get('/health')
async def health_check():
    return 'OK'


# Endpoint для отправки аудиофайла формата MP3 и получения результата распознавания в виде текста
@app.post('/recognize')
async def recognize(file: UploadFile = File(..., media_type="audio/mpeg")):
    # Конвертация MP3 в WAV и распознавание речи
    with open("temp_file.wav", "wb") as temp_file:
        temp_file.write(file.file.read())
    transcription = (asr("/content/temp_file.wav"))
    return transcription

# Для проверки кода в Google Collab можно использовать проксирование портов во вне:
'''
!ngrok config add-authtoken <PASTE TOKEN FROM https://dashboard.ngrok.com/get-started/your-authtoken HERE>

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
'''
