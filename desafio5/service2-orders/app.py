from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "✅ Serviço de Pedidos ativo!"})

@app.route("/orders")
def orders():
    return jsonify([
        {"id": 101, "user_id": 1, "produto": "Notebook", "valor": 4500.00},
        {"id": 102, "user_id": 2, "produto": "Ipad", "valor": 1000.00},
        {"id": 103, "user_id": 3, "produto": "PC gamer", "valor": 5000.00},
        {"id": 104, "user_id": 4, "produto": "mouse", "valor": 120.00},
        {"id": 105, "user_id": 5, "produto": "Monitor "", "valor": 1250.00}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
