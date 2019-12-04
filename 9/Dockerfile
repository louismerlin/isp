FROM python:3.7-alpine

COPY requirements.txt /
RUN pip3 install pptree

ADD miner /miner/
WORKDIR /miner

ENTRYPOINT ["./miner.py"]
