FROM python:3.10.7-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python"]

CMD ["home.py"]

