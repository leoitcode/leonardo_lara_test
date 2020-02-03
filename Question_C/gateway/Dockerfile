FROM python:3.7

WORKDIR /code 

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py ./

COPY gateway.py ./

CMD ["flask", "run", "--host=0.0.0.0"]
