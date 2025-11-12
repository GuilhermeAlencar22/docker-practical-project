from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API Gateway ativo! Use /users ou /orders."})

@app.route("/users")
def get_users():
    try:
        response = requests.get("http://service1:5001/users")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/orders")
def get_orders():
    try:
        response = requests.get("http://service2:5002/orders")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
