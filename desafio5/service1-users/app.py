from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "✅ Serviço de Usuários ativo!"})

@app.route("/users")
def users():
    return jsonify([
        {"id": 1, "nome": "Guilherme Alencar", "email": "guilherme@cesar.com"},
        {"id": 2, "nome": "Mariana Costa", "email": "mariana@cesar.com"},
        {"id": 3, "nome": "Lucas Mendes", "email": "lucas@cesar.com"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
