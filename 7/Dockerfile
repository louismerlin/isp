FROM python:3.8.0-alpine

RUN pip install requests==2.22.0 phe==1.4.0

COPY steal.py ./

CMD ["python", "steal.py"]
