FROM python:3.10.13-alpine3.18

RUN mkdir /app
WORKDIR /app

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
