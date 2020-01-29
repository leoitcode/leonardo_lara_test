FROM python:3

WORKDIR /app

RUN apt-get update && apt-get -y install netcat && apt-get clean

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY client_USA.py ./

COPY config.yml ./

RUN nameko run --config config.yml client_USA
