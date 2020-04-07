from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
login = LoginManager(app)
# куда будет перенапрявляться пользователь если он не авторизован ("login"-название функции во views)
login.login_view = 'login'
CSRF_ENABLED = True

from config import Config
app.config.from_object(Config)  # Подключаем наш конфиг


db = SQLAlchemy(app)

from app import views, models




