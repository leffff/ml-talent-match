FROM python:3.11.7-alpine

WORKDIR /code

COPY requirements/bot.txt requirements/bot.txt
COPY requirements/ml.txt requirements/ml.txt

RUN pip3 install -r requirements/bot.txt

COPY . /code

RUN mkdir -p /data/logs