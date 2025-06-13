import os


class Config:
    # Tenta pegar a variável DATABASE_URL do ambiente
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:123456@localhost:5432/alunosdb"
    )

    # Remove warnings desnecessários do SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
