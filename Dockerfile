FROM python:3.10.7-alpine3.16

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ['python']

CMD ['home.py']

