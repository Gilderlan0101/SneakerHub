from flask import Flask, Blueprint
from aplication.database.user import add_user,get_users

app = Flask(__name__)

login_ = Blueprint('login', __name__, template_folder='templates')

@login_.route("/login/", methods=["GET"])
def page_login():

    add_user('John Doe')
    users = get_users()
    print("Usuários no banco de dados:")
    for user in users:
        print(f"ID: {user['id']}, Nome: {user['name']}")

    return f"ID: {user['id']}, Nome: {user['name']}"

