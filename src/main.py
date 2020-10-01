from decouple import config
import psycopg2

conn = psycopg2.connect(
    host=config('DB_HOST'),
    port=config('DB_PORT'),
    user=config('DB_USER'),
    password=config('DB_PASSWORD'),
)

conn.autocommit = True

cursor = conn.cursor()

cursor.execute(f"DROP DATABASE IF EXISTS {config('DB_NAME')}")
cursor.execute(f"CREATE DATABASE {config('DB_NAME')}")

conn.autocommit = False
cursor.close()
conn.close()
