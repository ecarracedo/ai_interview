# Evaluador IA con LangChain
# Usa LangChain para hacerle una pregunta al modelo de lenguaje (GPT).
# Le pasa la pregunta, la respuesta esperada y lo que respondió el usuario.
# Devuelve si está correcta o no (basado en el análisis del LLM).
# Esto permite usar GPT como un evaluador flexible, más potente que un simple == entre strings.


from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import os

llm = ChatOpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))

template = PromptTemplate.from_template("""
Pregunta: {question}
Respuesta esperada: {correct_answer}
Respuesta del postulante: {user_answer}

¿La respuesta es correcta? Responde solo con "Sí" o "No".
""")

def is_answer_correct(question, correct_answer, user_answer):
    prompt = template.format(
        question=question,
        correct_answer=correct_answer,
        user_answer=user_answer
    )
    response = llm.invoke(prompt).content.strip().lower()
    return response.startswith("sí")
