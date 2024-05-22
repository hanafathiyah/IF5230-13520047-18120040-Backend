FROM python:3.9-alpine3.19

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

WORKDIR /app/api

CMD [ "python", "server.py" ]
