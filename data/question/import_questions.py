import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

# Leer el archivo CSV
df = pd.read_csv("data.csv")

# Conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
cur = conn.cursor()

# Insertar cada fila en la tabla 'questions'
for _, row in df.iterrows():
    cur.execute(
        """
        INSERT INTO questions (role, question, correct_answer)
        VALUES (%s, %s, %s)
        """,
        (row["Category"].strip(), row["Questions"].strip(), row["Answers"].strip())
    )

# Confirmar cambios y cerrar conexión
conn.commit()
cur.close()
conn.close()

print("✅ Datos importados correctamente en la tabla 'questions'.")
