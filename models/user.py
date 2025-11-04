from database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    # Definindo a tabela 'user' no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="user")
