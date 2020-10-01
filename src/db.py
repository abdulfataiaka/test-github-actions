from decouple import config
import psycopg2

class DB:
    @classmethod
    def connect(cls, dbname=False):
        params = dict(
            host=config('DB_HOST'),
            port=config('DB_PORT'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
        )

        if dbname:
            params['dbname'] = config['DB_NAME']

        return psycopg2.connect(**params)

    @classmethod
    def create(cls):
        conn = cls.connect()
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(f"DROP DATABASE IF EXISTS {config('DB_NAME')}")
        cursor.execute(f"CREATE DATABASE {config('DB_NAME')}")
        conn.autocommit = False
        cursor.close()
        conn.close()
