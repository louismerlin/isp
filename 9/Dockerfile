FROM python:3.7-alpine

RUN pip3 install pptree requests flask

ADD miner /miner/
WORKDIR /miner

ENTRYPOINT ["python", "miner.py"]
