FROM python:3.12-bullseye

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

WORKDIR /app/api

CMD [ "python", "server.py" ]
