# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем все остальные файлы проекта
COPY . .

# Выполняем тесты
CMD ["bash", "-c", "python -m unittest discover -s tests && python main.py"]
