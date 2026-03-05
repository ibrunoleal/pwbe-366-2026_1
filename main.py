from flask import Flask


app = Flask(__name__)


# Funcao de tratamento da requisicao. Pode pegar e tratar parametros e 
# deve obrigatoriamente retornar uma resposta (response).
def hello_world():
    return "<p>Hello, World!</p>"


# Regra de roteamento.
app.add_url_rule(
    rule="/hello", endpoint="hello", view_func=hello_world, methods=["GET"]
)
