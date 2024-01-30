!pip install -q condacolab
import condacolab
condacolab.install()

!conda install transformers fastapi huggingsound soundfiletransformers io torch python-multipart nest-asyncio pyngrok uvicorn pydub

from huggingsound import SpeechRecognitionModel
from transformers import Wav2Vec2Processor
from fastapi import FastAPI, HTTPException, File, UploadFile
import soundfile as sf
import numpy as np

model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-russian")
processor = Wav2Vec2Processor.from_pretrained("jonatasgrosman/wav2vec2-large-xlsr-53-russian")

udio_paths = ["/content/temp_file.wav"]
transcriptions = model.transcribe(audio_paths)
text = transcriptions[0]
print(text['transcription'])

rom transformers import pipeline
pipe = pipeline("automatic-speech-recognition", model="jonatasgrosman/wav2vec2-large-xlsr-53-russian")

app = FastAPI()
@app.get('/health')
async def health_check():
    return 'OK'

@app.post('/recognize')
async def recognize(file: UploadFile = File(..., media_type="audio/mpeg")):
	with open("temp_file.wav", "wb") as temp_file:
      	  temp_file.write(file.file.read())

transcription = (pipe("/content/temp_file.wav"))
    return {transcription}

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
