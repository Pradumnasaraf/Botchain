FROM python:3.7.3-alpine3.9
WORKDIR /app
COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "app/btc.py"]