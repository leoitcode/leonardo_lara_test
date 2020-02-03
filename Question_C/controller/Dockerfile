FROM python:3.7

WORKDIR /code

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY controller.py ./

COPY config.yml ./

CMD ["nameko", "run", "--config", "config.yml", "controller"]
