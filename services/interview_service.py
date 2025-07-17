# Lógica principal de entrevista
# Controla el proceso completo:

# - Obtiene las preguntas.
# - Llama al evaluador para cada una.
# - Calcula el score total.
# - Devuelve si el usuario pasó o no.

from models.question import get_random_questions
from agents.evaluator import is_answer_correct

def run_interview(role: str, user_answers: list[str]):
    questions = get_random_questions(role, len(user_answers))
    correct = 0

    for q, user_answer in zip(questions, user_answers):
        if is_answer_correct(q["question"], q["correct_answer"], user_answer):
            correct += 1

    score = correct / len(user_answers)
    return score >= 0.8, score
