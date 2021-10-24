import csv
from flask import Flask, json, jsonify, request

app = Flask(__name__)

db = []

@app.route('/', methods=['GET'])
def index():
    return 'Aplicando estudos realizados em Flask, criando uma simples API.'

@app.route('/get-all', methods=['GET'])
def get_all():
    return jsonify(db) if db != [] else jsonify({'message': 'nenhum registro encontrado!'})

@app.route('/import-csv', methods=['GET'])
def import_csv():
    try:
        with open('data.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            data = list(csv_reader)
            for produto in data:
                db.append(produto)
            return jsonify({'status': 'ok', 'message': 'dados importados com sucesso.'})
    except Exception:
        return jsonify({'status': 'error', 'message': 'verifique os dados informados e tente novamente!'})

@app.route('/export-csv', methods=['GET'])
def export_csv():
    try:
        with open('products.csv', 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=['id', 'name', 'price', 'quantity'], delimiter=';')
            csv_writer.writeheader()
            for product in db:
                csv_writer.writerow(product)
            return jsonify({'status': 'ok', 'message': 'dados exportados com sucesso.'})
    except Exception:
        return jsonify({'status': 'error', 'message': 'verifique os dados informados e tente novamente!'})

@app.route('/product/<id>', methods=['GET'])
def search_product(id):
    for product in db:
        if product['id'] == id:
            return product
    return jsonify({'status': 'error', 'message': 'o produto nao foi localizado!'})

@app.route('/create-product', methods=['POST'])
def create_product():
    try:
        data = request.json
        if data['id'] in [produto['id'] for produto in db]:
            return jsonify({'status': 'error', 'message': 'produto já existente!'})
        else:
            db.append(data)
            return jsonify({'status': 'ok', 'message': 'produto criado com sucesso.'})
    except Exception:
        return jsonify({'status': 'error', 'message': 'verifique os dados informados e tente novamente!'})

@app.route('/update-product', methods=['PUT'])
def update_product():
    try:
        data = request.json
        for product in db:
            if product['id'] == data['id']:
                product['name'] = data['name']
                product['price'] = data['price']
                product['quantity'] = data['quantity']
                return jsonify({'status': 'ok', 'message': 'dados alterados com sucesso.'})
        return jsonify({'status': 'error', 'message': 'nenhum produto encontrado!'})
    except Exception:
        return jsonify({'status': 'error', 'message': 'verifique os dados informados e tente novamente!'})

@app.route('/delete-product/<id>', methods=['DELETE'])
def delete_product(id):
    try:
        for product in db:
            if product['id'] == id:
                db.remove(product)
                return jsonify({'status': 'ok', 'message': 'produto removido com sucesso.'})
    except Exception:
        return jsonify({'status': 'error', 'message': 'o produto nao foi localizado!'})

if __name__ == '__main__':
    app.run(debug=True)