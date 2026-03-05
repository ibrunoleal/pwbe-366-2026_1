from flask import Flask
from flask import request


def hello_aluno():
    if request.method == 'GET':
        if len(request.args) == 0:
            return "Ola aluno sem nome (GET)!"
        else:
            nome = request.args.get('nome')
            return "Ola aluno {} com nome (GET)".format(nome)
    else:
        if request.method == 'POST':
            if len(request.form) == 0:
                return "Ola aluno sem nome (POST)!"
            else:
                nome = request.form.get('nome')
                return "Ola aluno {} com nome (POST)".format(nome)


# tratamento de rota com requisicao com metodo HTTP tipo GET
def hello_aluno_com_nome():
    nome = request.args.get('nome')
    return "Ola aluno {} (GET)".format(nome)


# tratamento de rota com requisicao com metodo HTTP tipo POST
def hello_aluno_com_nome_v2():
    nome = request.form.get('nome')
    return "Ola aluno {} (POST)".format(nome)


def adicionar_rotas(app: Flask):
    app.add_url_rule(
        rule="/aluno/hello",
        endpoint="hello_aluno",
        view_func=hello_aluno,
        methods=["GET", "POST"],
    )
    app.add_url_rule(
        rule="/aluno/hello_com_nome",
        endpoint="hello_aluno_com_nome",
        view_func=hello_aluno_com_nome,
        methods=["GET"],
    )
    app.add_url_rule(
        rule="/aluno/hello_com_nome_v2",
        endpoint="hello_aluno_com_nome_v2",
        view_func=hello_aluno_com_nome_v2,
        methods=["POST"],
    )
    