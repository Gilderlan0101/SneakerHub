from flask import Blueprint

register_ = Blueprint('register', __name__, template_folder='templates' )



@register_.route("/regisiter/")
def page_login():
    return "this page register"