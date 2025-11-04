from flask import Flask
from models.user import User
from database import db

# default app setup, sempre fazer.
app = Flask(__name__)
app.config["SECRET_KEY"] = "minha_key"  # Configurando chave bd
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///database.db"  # Configurando URI do banco de dados
)
db.init_app(app)  # Inicializando o banco de dados com a aplicação Flask


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
