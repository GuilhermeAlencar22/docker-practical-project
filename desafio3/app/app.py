from flask import Flask, jsonify
import psycopg2
import redis
import os

app = Flask(__name__)
DB_HOST = os.getenv("DATABASE_HOST")
DB_USER = os.getenv("DATABASE_USER")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")
DB_NAME = os.getenv("DATABASE_NAME")
CACHE_HOST = os.getenv("CACHE_HOST")

cache = redis.Redis(host=CACHE_HOST, port=6379)

def get_employees():
    """Retorna lista de funcionários do PostgreSQL com cache Redis"""
    cached_data = cache.get("funcionarios")

    if cached_data:
        print("✅ Retornando do cache")
        return eval(cached_data)

    print("📦 Consultando banco de dados...")
    conn = psycopg2.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, dbname=DB_NAME
    )
    cur = conn.cursor()
    cur.execute("SELECT id, nome, cargo FROM funcionarios;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    cache.set("funcionarios", str(rows), ex=30)  # cache expira em 30s
    return rows

@app.route("/")
def home():
    return jsonify({"status": "Aplicação rodando", "serviços": ["web", "db", "cache"]})

@app.route("/funcionarios")
def funcionarios():
    data = get_employees()
    return jsonify({"dados": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
