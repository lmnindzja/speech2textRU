# Модуль №4. Пример web-приложения машинного обучения для распознавания текста из аудио, развёрнутого в облаке

 Используются библиотеки:

- [huggingface](https://huggingface.co) - коллекция готовых обученных моделей
- [Streamlit](https://streamlit.io/) - для создания веб-приложения
- [transformers](https://huggingface.co/docs/transformers/index) - API и инструменты для простой интеграции предварительно обученных моделей


Для распознавания использована модель whisper-small (содержит  38 млн параматеров) из библиотеки huggingface [whisper-small](https://huggingface.co/openai/whisper-small)

При загрузке аудиофайла приложение использует ASR для распознавания речи и выводит полученный текст.

Приложение развернуто в яндекс.облаке на виртуальной машине по адресу http://158.160.24.95:8501/

Скриншот работы приложения
![image](https://github.com/lmnindzja/speech2textRU/assets/149816540/45bb2905-2c1b-4aa4-a963-8ac78825110f)
