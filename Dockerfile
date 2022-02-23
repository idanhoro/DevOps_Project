# syntax=docker/dockerfile:1
FROM python:3.10-bullseye
WORKDIR /code

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src/ /code

CMD ["python3", "/code/main.py"]
