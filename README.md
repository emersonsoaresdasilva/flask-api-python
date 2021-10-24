<h1><img src = "https://i.imgur.com/iEnfXJy.png" width="20%"/></h1>

<strong>Flask</strong> é um pequeno framework web escrito em Python. 

É classificado como um microframework porque não requer ferramentas ou bibliotecas particulares, mantendo um núcleo simples, porém, extensível.

### Ferramentas utilizadas:
- Python. 🐍
- Flask. 🌶️

### Descrição da API:
```json
{   
    "id": "1",
    "name": "Product test",
    "price": "100.00",
    "quantity": "10"
}
```
- [x] <strong>GET</strong>/get-all/:                A rota retorna todos os produtos cadastrados.
- [x] <strong>GET</strong>/import-csv/:             A rota importa dados de CSV.
- [x] <strong>GET</strong>/export-csv/:             A rota exporta dados em CSV.
- [x] <strong>GET</strong>/product/:id::            A rota retorna um produto.
- [x] <strong>POST</strong>/create-product:         A rota cria um produto.
- [x] <strong>PUT</strong>/update-product:          A rota atualiza um produto.
- [x] <strong>DELETE</strong>/delete-product/:id::  A rota deleta um produto.

### Executar servidor:
<code>python -m venv venv</code> ⤵

<code>venv\Scripts\activate</code>

<code>pip install -r requirements.txt</code>

<code>python .\app\app.py</code> ✔

### Requisitos para utilizar os scripts:
- [x] Ter o Python 3 instalado na máquina.
- [x] Saber lidar com venv e instalar as dependencias a partir do requirements.txt