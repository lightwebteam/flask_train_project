# import os
from app import app

class Config(object):
    app.config['SECRET_KEY'] = 'this-is-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:2378951@localhost/flask_train'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False