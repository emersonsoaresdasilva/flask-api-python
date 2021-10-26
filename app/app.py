import csv
import sql as db
from flask import Flask, json, jsonify, request

store = Flask(__name__)

@store.route('/', methods=['GET'])
def index():
    return 'Aplicando estudos realizados em Flask, criando uma simples API.'

@store.route('/get-all', methods=['GET'])
def get_all():
    return jsonify(db.get_all_products()) if db.get_all_products() else jsonify({'status': 'nenhum produto encontrado!'})

@store.route('/import-csv', methods=['POST'])
def import_csv():
    try:
        with open('store.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            data = list(csv_reader)
            for product in data:
                db.create_product(product)
            return jsonify({'status': 'ok', 'message': 'dados importados com sucesso.'})
    except Exception:
        return jsonify({'status': 'error', 'message': 'dados não localizados, verifique seu diretório.'})

@store.route('/export-csv', methods=['POST'])
def export_csv():
    try:
        with open('products.csv', 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=['id', 'name', 'price', 'quantity'], delimiter=';')
            csv_writer.writeheader()
            for product in db.get_all_products():
                csv_writer.writerow(product)
            return jsonify({'status': 'ok', 'message': 'dados exportados com sucesso.'})
    except Exception:
        return jsonify({'status': 'error', 'message': 'verifique os dados informados e tente novamente!'})

@store.route('/product/<int:id>', methods=['GET'])
def search_product(id):
    try:
        return jsonify(db.get_product(id))
    except Exception:
        return jsonify({'status': 'error', 'message': 'verifique os dados informados e tente novamente!'})

@store.route('/create-product', methods=['POST'])
def create_product():
    try:
        db.create_product(request.json)
        return jsonify({'status': 'ok', 'message': 'produto criado com sucesso!'})
    except Exception:
        return jsonify({'status': 'error', 'message': 'verifique os dados informados e tente novamente!'})

@store.route('/update-product/<int:id>', methods=['PUT'])
def update_product(id):
    db.update_product(request.json, id)
    return jsonify({'status': 'ok', 'message': 'produto atualizado com sucesso!'})

@store.route('/delete-product/<int:id>', methods=['DELETE'])
def delete_product(id):
    db.delete_product(id)
    return jsonify({'status': 'ok', 'message': 'produto removido com sucesso.'})

@store.route('/reset-products', methods=['POST'])
def reset_products():
    db.reset_products()
    return jsonify({'status': 'ok', 'message': 'produtos removidos com sucesso.'})

if __name__ == '__main__':
    store.run(debug=True)