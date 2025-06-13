from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Aluno
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
# CORS(app, origins=["http://localhost:5173"])
CORS(app)

def create_tables():
    with app.app_context():
        db.create_all()

@app.route("/alunos", methods=["POST"])
def criar_aluno():
    data = request.json
    novo_aluno = Aluno(**data)
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({"id": novo_aluno.id}), 201

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([{
        "id": a.id, "nome": a.nome, "email": a.email,
        "nota1": a.nota1, "nota2": a.nota2,
        "nota3": a.nota3, "nota4": a.nota4
    } for a in alunos])

@app.route("/alunos/<int:id>", methods=["GET"])
def obter_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    return jsonify({
        "id": aluno.id, "nome": aluno.nome, "email": aluno.email,
        "nota1": aluno.nota1, "nota2": aluno.nota2,
        "nota3": aluno.nota3, "nota4": aluno.nota4
    })

@app.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    data = request.json
    for campo in ["nome", "email", "nota1", "nota2", "nota3", "nota4"]:
        if campo in data:
            setattr(aluno, campo, data[campo])
    db.session.commit()
    return jsonify({"msg": "Aluno atualizado"})

@app.route("/alunos/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return jsonify({"msg": "Aluno deletado"})

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)
