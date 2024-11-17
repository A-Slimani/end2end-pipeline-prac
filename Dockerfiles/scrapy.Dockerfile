FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ../ufcstats . 

WORKDIR /app/ufcstats

# ENTRYPOINT [ "scrapy" ]