from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users')
def get_users():
    users = [
        {"id": 1, "nome": "Guilherme Alencar", "ativo_desde": "2021-09-15"},
        {"id": 2, "nome": "Mariana Costa", "ativo_desde": "2022-02-10"},
        {"id": 3, "nome": "Lucas Mendes", "ativo_desde": "2020-12-01"}
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
