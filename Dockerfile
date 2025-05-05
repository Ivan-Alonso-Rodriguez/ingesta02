FROM python:3-slim
WORKDIR /programas/ingesta
COPY . .
RUN pip install boto3 mysql-connector
CMD [ "python3", "./ingesta.py" ]
