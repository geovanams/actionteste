# Container image that runs your code
FROM ubuntu:latest

RUN sudo apt-get update

RUN sudo apt install python3

RUN sudo pip install requests

COPY main.py /main.py

CMD ["python", "main.py"]
