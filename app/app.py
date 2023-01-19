from flask import Flask
from flask import jsonify
from flask import request
from flask import current_app

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'x-super-secret'
    return app