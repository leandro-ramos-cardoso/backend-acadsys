from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Aluno
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Libera CORS para o frontend na Render

# MASTER
# CORS(app, resources={r"/*": {"origins": "https://react-frontend-acadsys.onrender.com"}}, supports_credentials=True)

# DEV
CORS(app)

# Inicializa banco
db.init_app(app)

# Cria a tabela automaticamente ao iniciar o app
with app.app_context():
    db.create_all()

# ROTAS

# GET /alunos → listar todos
@app.route("/alunos", methods=["GET"])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([{
        "id": a.id, "nome": a.nome, "email": a.email,
        "nota1": a.nota1, "nota2": a.nota2,
        "nota3": a.nota3, "nota4": a.nota4
    } for a in alunos])

# GET /alunos/<id> → buscar aluno por ID
@app.route("/alunos/<int:id>", methods=["GET"])
def obter_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    return jsonify({
        "id": aluno.id, "nome": aluno.nome, "email": aluno.email,
        "nota1": aluno.nota1, "nota2": aluno.nota2,
        "nota3": aluno.nota3, "nota4": aluno.nota4
    })

# POST /alunos → criar novo aluno
@app.route("/alunos", methods=["POST"])
def criar_aluno():
    data = request.json
    novo_aluno = Aluno(**data)
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({"id": novo_aluno.id}), 201

# PUT /alunos/<id> → atualizar aluno
@app.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    data = request.json
    for campo in ["nome", "email", "nota1", "nota2", "nota3", "nota4"]:
        if campo in data:
            setattr(aluno, campo, data[campo])
    db.session.commit()
    return jsonify({"msg": "Aluno atualizado"})

# DELETE /alunos/<id> → remover aluno
@app.route("/alunos/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return jsonify({"msg": "Aluno deletado"})

# ... todo o código que você já mandou acima ...
if __name__ == "__main__":
    app.run(debug=True)
