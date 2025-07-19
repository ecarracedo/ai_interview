from fastapi import FastAPI, HTTPException
from db import SessionLocal
from models import Question
from routers import evaluate
import random

app = FastAPI()
app.include_router(evaluate.router)

@app.get("/questions/{role_id}")
def get_random_questions(role_id: int, n: int = 10):
    db = SessionLocal()
    try:
        questions = db.query(Question).filter(Question.role_id == role_id).all()
        if not questions:
            raise HTTPException(status_code=404, detail="No questions found for this role.")

        sampled = random.sample(questions, min(n, len(questions)))
        return [{"id": q.id, "question": q.question} for q in sampled]
    finally:
        db.close()


