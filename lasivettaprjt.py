from transformers import pipeline
model = pipeline(model="seara/rubert-tiny2-ru-go-emotions")
model("Съешь еще этих мягких французских булок, да выпей чаю!")
