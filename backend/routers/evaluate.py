from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy.orm import Session
from db import get_db
from models import Question
import numpy as np

router = APIRouter()

# Cargar el modelo de SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")

# Definir el modelo de solicitud para la evaluación
class EvaluationRequest(BaseModel):
    question_id: int
    user_answer: str

# Ruta para evaluar la respuesta del usuario
@router.post("/evaluate")
def evaluate_answer(data: EvaluationRequest, db: Session = Depends(get_db)):
    """
    Evaluar la respuesta del usuario comparándola con la respuesta correcta de la base de datos
    """
    # Obtener la pregunta de la base de datos
    question = db.query(Question).filter(Question.id == data.question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")

    # Calcular la similitud entre la respuesta del usuario y la respuesta correcta

    user_embedding = model.encode(data.user_answer)
    expected_embedding = model.encode(question.answer)
   

    similarity = cosine_similarity([user_embedding], [expected_embedding])[0][0]
    similarity = float(similarity)
    
    if similarity >= 0.6:
        is_correct = True
    else:
        is_correct = False  
    
    return {
        "correct": is_correct,
        "similarity": round(similarity, 1)*100,
        "user_answer": data.user_answer,
        "expected_answer": question.answer
    }
