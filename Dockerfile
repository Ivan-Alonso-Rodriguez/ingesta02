FROM python:3-slim
WORKDIR /programas/ingesta
# Instalación de dependencias del sistema necesarias para compilar mysql-connector
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev
COPY . .
RUN pip install boto3 mysql-connector-python
CMD [ "python3", "./ingesta.py" ]
