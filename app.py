from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user

# default app setup, sempre fazer.
app = Flask(__name__)
app.config["SECRET_KEY"] = "minha_key"  # Configurando chave bd
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///database.db"  # Configurando URI do banco de dados
)

login_manager = LoginManager()
db.init_app(app)  # Inicializando o banco de dados com a aplicação Flask
login_manager.init_app(
    app  # Inicializando o gerenciador de login com a aplicação Flask
)
login_manager.login_view = "login"  # view login


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # fazendo login
    if username and password:
        # busca cliente no banco de dados + valida se a senha bate.
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "Login successful!", "username": username}), 200

    return (
        jsonify({"message": "Wrong username or password!"}),
        400,
    )  # caso n forneça username ou senha


if __name__ == "__main__":
    app.run(debug=True)
