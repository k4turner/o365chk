FROM python:3-slim

RUN pip install --upgrade pip

WORKDIR /app

COPY o365chk.py .
COPY requirements.txt .

RUN pip install -r requirements.txt
CMD ["python", "o365chk.py -d"]
