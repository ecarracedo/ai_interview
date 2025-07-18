# Usamos Python oficial
FROM python:3.10-slim

WORKDIR /app

# Dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY . .

# Exponer puerto de Streamlit
EXPOSE 8501

# Punto de entrada definido en docker-compose (streamlit run …)
