# Модуль №2. Пример web приложения машинного обучения для распознования текста из аудио 

## Описание
Приложение используется для создания WEB сервера c GUI для распознавания речи с использованием предобученной модели [lorenzoncina/whisper-small-ru](https://huggingface.co/lorenzoncina/whisper-small-ru) (содержит  38 млн параматеров).
Пользователь может отправить аудиофайл на сервер, после чего возвращается распознанный текст.

 Используются библиотеки:

- [huggingface](https://huggingface.co) (коллекция готовых обученных моделей)
- [Streamlit](https://streamlit.io/) - для создания веб-приложения
- [transformers](https://huggingface.co/docs/transformers/index) -  инструменты для простой интеграции предварительно обученных моделей

Скриншот работы приложения

![image](https://github.com/lmnindzja/speech2textRU/assets/149816540/4ae686d3-1c9c-434b-b0c7-fc3c63629b7c)
