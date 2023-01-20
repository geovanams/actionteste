# Container image that runs your code
FROM ubuntu:latest

RUN apt-get update --force

RUN apt install python3 --force

RUN pip install requests --force

COPY main.py /main.py

CMD ["python", "main.py"]
