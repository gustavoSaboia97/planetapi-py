FROM python:3.8.5-alpine

WORKDIR /app

COPY . /app

RUN apk add build-base

RUN pip install -r requirements.txt

CMD ["uvicorn", "starter:app", "--host", "0.0.0.0", "--port", "8888"]