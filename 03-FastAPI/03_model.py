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

