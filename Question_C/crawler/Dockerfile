FROM python:3.6.8

WORKDIR /code

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords

COPY crawler.py ./

COPY config.yml ./

CMD ["nameko", "run", "--config", "config.yml", "crawler"]
