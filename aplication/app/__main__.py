# app_factory.py
from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("KEY")
    app.config["DEBUG"] = os.getenv("DEBUG")

    from aplication.routes.man.home_page import home_
    from aplication.routes.login.login_page import login_
    from aplication.routes.register.register_page import register_

    app.register_blueprint(home_)
    app.register_blueprint(login_)
    app.register_blueprint(register_)

    return app
