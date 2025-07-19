import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://backend:8000") # Cambiar por la URL real del backend si está en contenedor

st.title("Entrevista Técnica IA")


# Paso 1: seleccionar rol
roles = {"Data Science": 1}  # En el futuro se puede hacer dinámico desde la API
selected_role = st.selectbox("Selecciona el puesto al que deseas postularte:", list(roles.keys()))

if st.button("Comenzar entrevista"):
    # Paso 2: obtener preguntas del backend segun el rol seleccionado
    role_id = roles[selected_role]
    # Hacer la solicitud a la API para obtener las preguntas segun rol (rol_id)
    # Cantidad de preguntas (params) puede ser configurable
    response = requests.get(f"{API_URL}/questions/{role_id}", params={"n": 5})

    #questions = response.json() #Para debug, mostrar las preguntas obtenidas
    #st.json(questions)  # Para debug, mostrar las preguntas obtenidas
    
    if response.status_code != 200:
        st.error("Error al obtener las preguntas.")
    else:
        st.session_state.questions = response.json()
        st.session_state.answers = []
        st.session_state.current_index = 0
        st.session_state.correct = 0

# Si ya comenzó la entrevista
if "questions" in st.session_state:
    idx = st.session_state.current_index
    if idx < len(st.session_state.questions):
        q = st.session_state.questions[idx]
        st.subheader(f"Pregunta {idx + 1}")
        st.write(q["question"])
        user_answer = st.text_input("Tu respuesta:", key=f"answer_{idx}")

        if st.button("Siguiente"):
            st.session_state.answers.append(user_answer)
            # Aquí podrías traer y comparar con la respuesta correcta desde la API o incluirla en la respuesta inicial
            # Suponemos que ya vino la respuesta correcta (para MVP rápido)
            correct_answer = q.get("correct_answer", "").strip().lower()
            if user_answer.strip().lower() == correct_answer:
                st.session_state.correct += 1

            st.session_state.current_index += 1
            st.rerun()
    else:
        total = len(st.session_state.questions)
        correct = st.session_state.correct
        score = (correct / total) * 100
        st.success(f"Tu puntaje final: {score:.2f}%")
        if score >= 80:
            st.balloons()
            st.success("¡Felicitaciones! Pasaste a la siguiente etapa.")
        else:
            st.warning("Gracias por participar. En esta ocasión no pasaste al siguiente paso.")
        st.button("Reiniciar entrevista", on_click=lambda: st.session_state.clear())
