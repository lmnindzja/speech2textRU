from transformers import pipeline
!wget -O uploaded.mp3 http://www.moviesoundclips.net/movies1/backtothefuture/style.mp3
asr = pipeline("automatic-speech-recognition",   
                      "openai/whisper-small")


text = asr('uploaded.mp3')
print (text)

