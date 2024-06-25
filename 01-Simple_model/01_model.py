from transformers import pipeline
audio_link="http://www.moviesoundclips.net/movies1/backtothefuture/style.mp3"
asr = pipeline("automatic-speech-recognition",
                      "openai/whisper-small")


text = asr(audio_link)
print (text)
