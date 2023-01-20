# Container image that runs your code
FROM debian:latest

RUN apt-get update

RUN apt install python3

RUN pip install requests

COPY main.py /main.py

CMD ["python", "main.py"]
