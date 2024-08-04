# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY main.py /app/
COPY templates /app/templates/
COPY static /app/static/

RUN pip install pymongo

CMD ["python", "main.py"]

