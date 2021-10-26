from sqlalchemy import create_engine

engine = create_engine('sqlite:///store.db')

with engine.connect() as connection:
    create_product = '''
    CREATE TABLE IF NOT EXISTS Product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        price DECIMAL NOT NULL,
        quantity INTEGER NOT NULL
    )
    '''
    connection.execute(create_product)

def create_product(json):
    with engine.connect() as connection:
        connection.execute(
            '''INSERT INTO Product (name, price, quantity) VALUES (:name, :price, :quantity)''',
            json['name'],
            json['price'],
            json['quantity']
        )

def get_product(id):
    with engine.connect() as connection: 
        product = connection.execute('''SELECT * FROM Product WHERE id = :id''', id=id).fetchone()
        return dict(product) if product is not None else NotFoundError

def get_all_products():
    with engine.connect() as connection:
        products = connection.execute('''SELECT * FROM Product''').fetchall()
        products = [dict(product) for product in products]
        return products

def update_product(json, id):
    with engine.connect() as connection:
        connection.execute(
            '''UPDATE Product SET name = :name, price = :price, quantity = :quantity WHERE id = :id''',
            id=id,
            name=json['name'],
            price=json['price'],
            quantity=json['quantity']
        )
    
def delete_product(id):
    with engine.connect() as connection:
        connection.execute('''DELETE FROM Product WHERE id = :id''', id=id)

def reset_products():
    with engine.connect() as connection:
        connection.execute('''DELETE FROM Product''')