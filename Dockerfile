FROM python:3.10.6

ENV APP_HOME ./
WORKDIR $APP_HOME
COPY . ./

RUN pip3 install -r requirements.txt

CMD home:app

