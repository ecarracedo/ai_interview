# Acceso a datos del modelo
# Se conecta a la DB y trae preguntas aleatorias según el puesto.
# Encapsula la lógica de acceso a base de datos para que otras partes del 
# sistema no se acoplen a SQL directamente.

# get_random_questions("Data Science", n=10)

from config.db import get_connection

def get_random_questions(role: str, n: int = 10):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, question, correct_answer
        FROM questions
        WHERE role = %s
        ORDER BY RANDOM()
        LIMIT %s
    """, (role, n))
    result = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "question": r[1], "correct_answer": r[2]} for r in result]
