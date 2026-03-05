from flask import Flask

# routers
from routes import aluno_router, professor_router

app = Flask(__name__)

aluno_router.adicionar_rotas(app=app)
professor_router.adicionar_rotas(app=app)
