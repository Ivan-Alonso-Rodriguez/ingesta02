import boto3
import mysql
import csv

# Variables de conexion
DB_HOST = "localhost" # o otro host
DB_PORT = 3306
DB_USER = "tu-usuario"
DB_PASSWORD = "tu-clave"
DB_NAME = "tu-bd"
DB_TABLE = "tu-tabla"
BUCKET_NAME = "iarp-output-01"
FILE_NAME = "data.csv"

# Usando mysql-connector-python
conn = mysql.connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = conn.cursor()
cursor.execute(f"SELECT * FROM {DB_TABLE}")

# Escribe el csv para luego pasarlo
with open(FILE_NAME, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([i[0] for i in cursor.description])  # nombres de columnas
    for row in cursor.fetchall():
        writer.writerow(row)

cursor.close()
conn.close()

# Subimos a S3
s3 = boto3.client('s3')
s3.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)

print("Ingesta desde MySQL completada.")
