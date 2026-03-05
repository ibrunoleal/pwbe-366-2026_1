from flask import Flask


app = Flask(__name__)


# Funcao de tratamento da requisicao. Pode pegar e tratar parametros e
# deve obrigatoriamente retornar uma resposta (response).
def hello_world():
    return "<p>Hello, World!</p>"


def hello_aluno():
    return "Ola aluno!"


def hello_professor():
    return "Ola professor!"


# Regra de roteamento.
app.add_url_rule(
    rule="/hello", endpoint="hello", view_func=hello_world, methods=["GET"]
)
app.add_url_rule(
    rule="/professor/hello",
    endpoint="hello_professor",
    view_func=hello_professor,
    methods=["GET"],
)
app.add_url_rule(
    rule="/aluno/hello",
    endpoint="hello_aluno",
    view_func=hello_aluno,
    methods=["GET"],
)
