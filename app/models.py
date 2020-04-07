from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Test_table(db.Model):
    __tablename__ = 'test_table'
    # __table_args__ = ({"schema": "test_schema"})
    id = db.Column(db.Integer, index=True, primary_key=True)
    data = db.Column(db.String(20), index=True)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128), index=True)
    sex = db.Column(db.String(6), index=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

"""загрузчик пользователя"""
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

