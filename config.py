# import os
#
# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:123456@localhost:5432/alunosdb")
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://usuario:senha@localhost:5432/alunosdb")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
