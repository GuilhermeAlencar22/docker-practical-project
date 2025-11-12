from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/info')
def get_info():
    try:
        response = requests.get("http://service-a:5001/users")
        users = response.json()
        formatted = [
            f"Usuário {u['nome']} ativo desde {u['ativo_desde']}"
            for u in users
        ]
        return jsonify(formatted)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
