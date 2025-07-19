import streamlit as st
import requests

API_URL = "http://backend:8000"

# Mapear roles a IDs (según tu base de datos)
ROLE_MAP = {
    "Data Science": 1
    # Podés agregar más roles si los tenés cargados
}

st.title("🧠 Entrevista IA")

# Selección del rol
role_name = st.selectbox("Seleccioná un puesto:", list(ROLE_MAP.keys()))
role_id = ROLE_MAP[role_name]

# Botón para iniciar
if st.button("Comenzar entrevista"):
    response = requests.get(f"{API_URL}/questions/{role_id}", params={"n": 5})
    if response.status_code == 200:
        st.session_state.questions = response.json()
        st.session_state.answers = [""] * len(st.session_state.questions)
        st.session_state.similarities = []
    else:
        st.error("No se pudieron obtener las preguntas.")

# Mostrar preguntas y capturar respuestas
if "questions" in st.session_state and st.session_state.questions:
    st.subheader("Responde las siguientes preguntas:")

    for i, q in enumerate(st.session_state.questions):
        st.session_state.answers[i] = st.text_input(
            f"{i+1}. {q['question']}",
            value=st.session_state.answers[i],
            key=f"answer_{i}"
        )

    if st.button("Finalizar"):
        correct_count = 0
        st.session_state.similarities = []

        for i, q in enumerate(st.session_state.questions):
            user_answer = st.session_state.answers[i]
            payload = {
                "question_id": q["id"],
                "user_answer": user_answer
            }

            response = requests.post(f"{API_URL}/evaluate", json=payload)

            if response.status_code == 200:
                result = response.json()
                similarity = result["similarity"]
                st.session_state.similarities.append(similarity)

                st.write(f"➡️ Pregunta {i+1}")
                st.write("Respuesta del usuario:", user_answer)
                st.write("Respuesta esperada:", result.get("expected_answer"))
                st.write("Similaridad:", similarity)
                st.write("¿Correcta?", result["correct"])
                st.markdown("---")

                if result["correct"]:
                    correct_count += 1
            else:
                st.error(f"Error al evaluar la respuesta {i+1}")

        # Calcular puntaje final
        score = correct_count / len(st.session_state.questions)
        st.success(f"Resultado final: {score * 100:.0f}%")

        if score >= 0.60:
            st.balloons()
            st.info("✅ ¡Felicitaciones! Pasás a la siguiente etapa.")
        else:
            st.warning("❌ No alcanzaste el 60%. ¡Gracias por participar!")
