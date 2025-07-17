import streamlit as st
from models.question import get_random_questions
from services.interview_service import run_interview

st.title("🧠 Entrevista IA")

role = st.selectbox("Seleccioná un puesto:", ["Data Science"])  # Escalable
start = st.button("Comenzar entrevista")

if "questions" not in st.session_state:
    st.session_state.questions = []
    st.session_state.answers = []

if start:
    st.session_state.questions = get_random_questions(role)
    st.session_state.answers = [""] * len(st.session_state.questions)

if st.session_state.questions:
    for i, q in enumerate(st.session_state.questions):
        st.session_state.answers[i] = st.text_input(f"{i+1}. {q['question']}", value=st.session_state.answers[i])

    if st.button("Finalizar"):
        aprobado, score = run_interview(role, st.session_state.answers)
        st.success(f"Resultado: {score*100:.0f}%")
        if aprobado:
            st.balloons()
            st.info("✅ ¡Felicitaciones! Pasás a la siguiente etapa.")
        else:
            st.warning("❌ No alcanzaste el 80%. ¡Gracias por participar!")

