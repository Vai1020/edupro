from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__,template_folder='template', static_folder='static')
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
'''ID = ['OPTION A','OPTION B','OPTION C','OPTION D']
app.secret_key = "Huygens0p"
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'medical0377@gmail.com',
    MAIL_PASSWORD = 'mcdkwxkhxgopanrz',
))
mail = Mail(app)'''
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flaskblog import routes