from flask import Flask


def hello_aluno():
    return "Ola aluno!"


def adicionar_rotas(app: Flask):
    app.add_url_rule(
        rule="/aluno/hello",
        endpoint="hello_aluno",
        view_func=hello_aluno,
        methods=["GET"],
    )