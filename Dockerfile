FROM python:3.8-alpine3.18

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

WORKDIR /app/api

CMD [ "python", "server.py" ]
