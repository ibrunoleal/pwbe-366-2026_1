from flask import Flask
from flask import request

def hello_professor():
    if request.method == 'GET':
        if len(request.args) == 0:
            return "Ola professor sem nome (GET)!"
        else:
            nome = request.args.get('nome')
            return "Ola professor {} com nome (GET)".format(nome)
    else:
        if request.method == 'POST':
            if len(request.form) == 0:
                return "Ola professor sem nome (POST)!"
            else:
                nome = request.form.get('nome')
                return "Ola professor {} com nome (POST)".format(nome)


# tratamento de rota com requisicao com metodo HTTP tipo GET
def hello_professor_com_nome():
    nome = request.args.get('nome')
    return "Ola professor {} (GET)".format(nome)


# tratamento de rota com requisicao com metodo HTTP tipo POST
def hello_professor_com_nome_v2():
    nome = request.form.get('nome')
    return "Ola professor {} (POST)".format(nome)


def adicionar_rotas(app: Flask):
    app.add_url_rule(
        rule="/professor/hello",
        endpoint="hello_professor",
        view_func=hello_professor,
        methods=["GET", "POST"],
    )
    app.add_url_rule(
        rule="/professor/hello_com_nome",
        endpoint="hello_professor_com_nome",
        view_func=hello_professor_com_nome,
        methods=["GET"],
    )
    app.add_url_rule(
        rule="/professor/hello_com_nome_v2",
        endpoint="hello_professor_com_nome_v2",
        view_func=hello_professor_com_nome_v2,
        methods=["POST"],
    )
