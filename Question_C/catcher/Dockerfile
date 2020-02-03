FROM python:3.6

WORKDIR /code

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY catcher.py ./

COPY config.yml ./

CMD ["nameko", "run", "--config", "config.yml", "catcher"]
