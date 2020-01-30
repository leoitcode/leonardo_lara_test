FROM python:3

WORKDIR /app

RUN apt-get update && apt-get -y install netcat && apt-get clean

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY client_CAN.py ./

COPY config.yml ./

CMD ["nameko", "run", "--config", "config.yml", "client_CAN"]