from flask import Flask, request, jsonify
from models.user import User
from database import db
from dotenv import load_dotenv
import os
from flask_login import (
    LoginManager,
    login_user,
    current_user,
    logout_user,
    login_required,
)

# default app setup, sempre fazer.
load_dotenv()
app = Flask(__name__)
# Configurando chave bd e banco de dados
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
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


# fazendo lgion
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # fazendo logica login
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


# fazendo logout
@app.route("/logout", methods=["GET"])
@login_required  # apenas usuários logados podem fazer logout
def logout():
    logout_user()
    return jsonify({"message": "Logout successful!"}), 200


# criando usuario
@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username and password:
        if User.query.filter_by(username=username).first():
            return jsonify({"message": "Username already exists!"}), 400

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully!"}), 201

    return jsonify({"message": "Username and password are required!"}), 400


# pegando todos usuario
@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    users_list = [{"id": user.id, "username": user.username} for user in users]
    return jsonify(users_list), 200


# pegando usuario por id
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({"id": user.id, "username": user.username}), 200
    return jsonify({"message": "User not found!"}), 404


# atualizando senha do usuario
@app.route("/update_password", methods=["PUT"])
@login_required
def update_password():
    data = request.get_json()
    new_password = data.get("new_password")

    if new_password:
        current_user.password = new_password
        db.session.commit()
        return jsonify({"message": "Password updated successfully!"}), 200

    return jsonify({"message": "New password is required!"}), 400


# deletando usuario
@app.route("/delete_user", methods=["DELETE"])
@login_required  # apenas o próprio usuário logado pode deletar sua conta
def delete_user():
    data = request.get_json()
    username = data.get("username")

    user = User.query.filter_by(username=username).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "Your user was deleted successfully!"}), 200

    return jsonify({"message": "User not found!"}), 404


if __name__ == "__main__":
    app.run(debug=True)
