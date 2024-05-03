FROM python:3.11-slim

# Переменные окружения
ENV SCALER_PATH='/model/iris_scaler.pkl'
ENV MODEL_PATH='/model/iris_model.pkl'

# Копирование файлов проекта
COPY . /app

# Установка директории проета
WORKDIR /app

# Установка зависимостей
RUN pip install -r requirements.txt

# Обучение модели
RUN python3 /app/src/train_model.py

# Запуск приложения Streamlit
CMD ["streamlit", "run", "src/app.py", "--server.port=8081"]
