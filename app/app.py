from flask import Flask, json, jsonify, request

app = Flask(__name__)

db = []

@app.route('/', methods=['GET'])
def index():
    return 'Aplicando estudos realizados em Flask, criando uma simples API.'

@app.route('/get-all', methods=['GET'])
def get_all():
    return jsonify(db) if db != [] else jsonify({'message': 'nenhum registro encontrado!'})

if __name__ == '__main__':
    app.run(debug=True)