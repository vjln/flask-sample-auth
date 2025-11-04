from flask import Flask
from flask_sqlalchemy import (
    SQLAlchemy,
)  # importando SQLAlchemy para conectar com banco de dados

app = Flask(__name__)
app.config["SECRET_KEY"] = "sua_chave"  # Configurando chave bd
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///database.db"  # Configurando URI do banco de dados
)
db = SQLAlchemy(app)  # Inicializando SQLAlchemy com a aplicação Flask


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
