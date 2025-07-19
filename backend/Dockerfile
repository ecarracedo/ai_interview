# Usamos Python oficial
FROM python:3.10-slim

# Working directory
WORKDIR /app

# Instalar PyTorch solo para CPU (importante para evitar dependencias de CUDA)
#RUN pip install torch --index-url https://download.pytorch.org/whl/cpu --trusted-host download.pytorch.org

# Instalar sentence-transformers
#RUN pip install sentence-transformers

# Copiamos requirements y los instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY . .

# Exponemos el puerto de Uvicorn
EXPOSE 8000

# Punto de entrada definido en docker-compose (uvicorn main:app …)
