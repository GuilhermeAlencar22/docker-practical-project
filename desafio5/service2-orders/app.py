from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "✅ Serviço de Pedidos ativo!"})

@app.route("/orders")
def orders():
    return jsonify([
        {"id": 101, "user_id": 1, "produto": "Notebook", "valor": 4500.00},
        {"id": 102, "user_id": 2, "produto": "Teclado Mecânico", "valor": 520.00},
        {"id": 103, "user_id": 3, "produto": "Monitor 27\"", "valor": 1250.00}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
