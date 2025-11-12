# Imagem base
FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copiar arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Expor porta 8080
EXPOSE 8080

# Comando para iniciar o servidor Flask
CMD ["python", "app.py"]
