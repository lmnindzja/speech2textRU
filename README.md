# УРФУ 2024. Программная инженерия. Репозиторий команды π-24 
# Итоговый проект. speech2textRU
## Цель проекта
Целью данного проекта является разработка и реализация эффективного и точного сервиса транскрибации аудиозаписей с использованием искусственного интеллекта и машинного обучения. Этот сервис позволит студентам и другим пользователям преобразовывать аудиозаписи в текстовый формат. Наш сервис будет универсальным, легким в использовании и обеспечит высокое качество транскрибации, чтобы пользователи могли легко обрабатывать и анализировать информацию из аудиозаписей.

## Значимость проекта
В настоящее время в интернете доступно огромное количество информации в виде лекций, вебинаров и других аудиозаписей, которые могут быть использованы студентами в учебных целях. Однако часто у нас просто не хватает времени, чтобы прослушать или просмотреть все эти материалы. Наш проект предоставляет студентам удобный и эффективный способ преобразования аудиозаписей в текст, улучшая доступность, навигацию и анализ учебных материалов. Он поможет студентам сэкономить время и повысить эффективность своего обучения. Перевод аудиозаписей в текстовый формат позволяет:
- Упростить навигацию по материалу.
- Предоставлять доступ к информации людям с нарушениями слуха.
- Сравнивать и объединять информацию из разных источников.
- Некоторым людям проще воспринимать информацию в текстовом формате, чем в аудиоформате.

## Описание
speech2textRU - Приложение для конвертации аудио записей на русском языке в текст с WEB-Интерфейсом из библиотеки streamlit.

Функции по распознованию и конвертации речи выполняет модель [lorenzoncina/whisper-small-ru](https://huggingface.co/lorenzoncina/whisper-small-ru).
Данная модель представляет собой доработанную для преобразования русской речи в русский текст версию [openai/whisper-small](https://huggingface.co/openai/whisper-small). 
Дообучение проводилось на датасете mozilla-foundation/common_voice_11_0 ru. 

На проверочной выборке модель показывает следующий результат:
### Loss: 0.3060
### Wer: 12.2375

## Состав команды
1.  Каменский Сергей Вадимович - Менеджер проекта, Аналитик данных
2.  Алиев Владислав Вагифович - Программист-разработчик
3.  Ласковая Иветта Эдуардовна -  Full Stack-разработчик, Тестировщик-QA инженер
4.  Кондратьев Андрей Сергеевич - Документалист/технический писатель

