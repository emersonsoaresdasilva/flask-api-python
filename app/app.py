from flask import Flask, json, jsonify, request

app = Flask(__name__)

db = []

@app.route('/', methods=['GET'])
def index():
    return 'Aplicando estudos realizados em Flask, criando uma simples API.'

if __name__ == '__main__':
    app.run(debug=True)