FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]

#docker build -t app_1 .
# docker run -p 8000:8000 langchain-fastapi-app