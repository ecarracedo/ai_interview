# Conexión a PostgreSQL
# Usa las variables de .env para conectarse a PostgreSQL.
# Devuelve una conexión lista para usar con psycopg2.

import psycopg2
import os
from dotenv import load_dotenv



load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
