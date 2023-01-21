# Container image that runs your code
FROM python:3.8-slim-buster

COPY main.py /app/

WORKDIR /app

ENTRYPOINT ["python", "main.py"]
