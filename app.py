from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Aluno
from config import Config  # cuidado aqui: use `from config` e não `import config`

app = Flask(__name__)
app.config.from_object(Config)

# CORS liberado apenas para o frontend da Render
CORS(app, origins=["https://react-frontend-acadsys.onrender.com"])

# Inicializa o banco
db.init_app(app)

# Criação de tabela automática
@app.before_first_request
def create_tables():
    db.create_all()

# Rotas
@app.route("/alunos", methods=["GET"])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([{
        "id": a.id, "nome": a.nome, "email": a.email,
        "nota1": a.nota1, "nota2": a.nota2,
        "nota3": a.nota3, "nota4": a.nota4
    } for a in alunos])

@app.route("/alunos", methods=["POST"])
def criar_aluno():
    data = request.json
    novo_aluno = Aluno(**data)
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({"id": novo_aluno.id}), 201
