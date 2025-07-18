import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

# Leer el archivo CSV
df = pd.read_csv("data.csv")

# Conexión a PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
cur = conn.cursor()

# Insertar cada pregunta con role_id = 1 (Data Science)
inserted = 0
for _, row in df.iterrows():
    cur.execute(
        """
        INSERT INTO questions (role_id, question, correct_answer)
        VALUES (%s, %s, %s)
        """,
        (1, row["Questions"].strip(), row["Answers"].strip())
    )
    inserted += 1

conn.commit()
cur.close()
conn.close()

print(f"✅ Importación completada. Total preguntas insertadas: {inserted}")
