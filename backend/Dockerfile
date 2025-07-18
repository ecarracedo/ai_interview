# Usamos Python oficial
FROM python:3.10-slim

# Working directory
WORKDIR /app

# Copiamos requirements y los instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY . .

# Exponemos el puerto de Uvicorn
EXPOSE 8000

# Punto de entrada definido en docker-compose (uvicorn main:app …)
