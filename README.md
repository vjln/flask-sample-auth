# 🔐 Flask Auth API

API Python construída com **Flask**, usando **MySQL** como banco de dados e **bcrypt** para hash de senhas.  
O projeto inclui integração via **Docker Compose** e suporte a variáveis de ambiente através do **python-dotenv**.

---

## 🚀 Tecnologias

- 🐍 Python 3.13
- ⚙️ Flask
- 🧱 SQLAlchemy
- 🐬 MySQL (via Docker)
- 🔒 bcrypt (hash seguro de senhas)
- 🌿 python-dotenv
- 🐳 Docker Compose

---

## 📂 Estrutura do Projeto

```
flask-sample-auth/
│
├── app.py
├── database.py
├── models/
│   └── user.py
├── .env.example
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ Configuração do Ambiente

1. **Clone o repositório**

   ```bash
   git clone https://github.com/seu-usuario/flask-auth-api.git
   cd flask-auth-api
   ```

2. **Crie o arquivo `.env`**

   ```bash
   cp .env.example .env
   ```

   Edite as variáveis conforme seu ambiente:

   ```env
   # Flask
   FLASK_ENV=development
   SECRET_KEY=sua_chave_segura

   # MySQL
   DB_USER=admin
   DB_PASSWORD=senha123
   DB_NAME=db_flask_crud
   DB_HOST=127.0.0.1
   DB_PORT=3306
   ```

3. **Suba o banco de dados com Docker**

   ```bash
   docker compose up -d
   ```

4. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

5. **Inicie o servidor Flask**
   ```bash
   python ./app.py
   ```

---

## 🔗 Endpoints da API

| Método   | Rota                             | Descrição                      |
| -------- | -------------------------------- | ------------------------------ |
| `POST`   | `/login`                         | Autentica um usuário existente |
| `GET`    | `/logout`                        | Encerra a sessão do usuário    |
| `POST`   | `/user`                          | Cria um novo usuário           |
| `GET`    | `/users`                         | Retorna todos os usuários      |
| `GET`    | `/users/<int:user_id>`           | Retorna um usuário específico  |
| `PUT`    | `/update_password/<int:user_id>` | Atualiza a senha de um usuário |
| `DELETE` | `/delete_user/<int:user_id>`     | Remove um usuário pelo ID      |

---

## 🧪 Exemplos de uso (Postman)

A coleção completa está disponível aqui:  
[📬 Postman Collection – flask-api-auth](https://vitorjorgeln-dev-3321789.postman.co/workspace/Vitor-Leal's-Workspace~11a978ae-269c-4c07-89b1-d006315bd7e8/collection/47400012-77266b9c-cf2f-4293-925d-d7c5dd3f1896?action=share&source=collection_link&creator=47400012)

### Exemplo — Criação de Usuário

```
POST /user
Content-Type: application/json

{
  "username": "user",
  "password": "pass"
}
```

### Exemplo — Login

```
POST /login
Content-Type: application/json

{
  "username": "user",
  "password": "pass"
}
```

### Exemplo — Atualização de Senha

```
PUT /update_password/1
Content-Type: application/json

{
  "new_password": "novaSenha"
}
```

---

## 🔒 Segurança das Senhas

As senhas são armazenadas de forma segura usando **bcrypt** com salt:

```python
import bcrypt

hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
bcrypt.checkpw(password.encode("utf-8"), hashed_password)
```

---

## 🧰 Docker Compose

Arquivo `docker-compose.yml`:

```yaml
services:
  db:
    image: mysql:latest
    restart: always
    environment:
      MYSQL_USER: ${DB_USER}
      MYSQL_PASSWORD: ${DB_PASSWORD}
      MYSQL_DATABASE: ${DB_NAME}
      MYSQL_ROOT_PASSWORD: ${DB_PASSWORD}
    volumes:
      - D:\code\repos\studies\python\mysql:/var/lib/mysql
    ports:
      - "${DB_PORT}:3306"
    expose:
      - "3306"
```

---

## 🧑‍💻 Autor

**Vítor Nascimento**  
Desenvolvedor de Chatbots & AI

---

## 📜 Licença

Este projeto está sob a licença MIT — sinta-se livre para usar e modificar.  
Veja o arquivo `LICENSE` para mais detalhes.

---

> Feito com ☕ e Flask.
