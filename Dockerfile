FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y flac && rm -rf /var/lib/apt/lists/*
RUN apt update && apt install -y ffmpeg

CMD exec gunicorn --bind :$PORT --workers 5 --threads 2 --timeout 0 home:app


