from flask import Blueprint

home_ = Blueprint('home', __name__, template_folder='templates' )



@home_.route("/")
def page_home():
    return "Ola mundo"