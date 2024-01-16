# Container image that runs your code2
FROM python:3.8-alpine

RUN pip install requests

COPY main.py /main.py

ENTRYPOINT ["python", "/main.py"]
