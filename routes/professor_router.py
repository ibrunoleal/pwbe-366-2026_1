from flask import Flask

def hello_professor():
    return "Ola professor!"

def adicionar_rotas(app: Flask):
    app.add_url_rule(
        rule="/professor/hello",
        endpoint="hello_professor",
        view_func=hello_professor,
        methods=["GET"],
    )
