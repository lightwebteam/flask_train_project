from app.models import Test_table

"""эти модули отвечают за работу с формами"""
from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class TestForm(FlaskForm):
    test_form = wtforms.StringField('Тестовый ввод данных', validators=[DataRequired()])
    submit = wtforms.SubmitField('Отправка данных на сервер')

    def validate_test_form(self, test_form):
        letter = Test_table.query.filter(Test_table.data == test_form.data).first()
        """если что-то нашли"""
        if letter is not None:
            raise ValidationError('Такое значение уже есть')


class Register(FlaskForm):
    username = wtforms.StringField('Имя пользователя', validators=[DataRequired()])
    email = wtforms.StringField('Почта', validators=[DataRequired(), Email()])
    password = wtforms.StringField('Пароль', validators=[DataRequired()])
    repeat_password = wtforms.StringField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    sex = wtforms.SelectField('Выберите пол', choices=[('male', 'Мужчина'), ('female', 'Женщина')])
    submit = wtforms.SubmitField('Регистрация')
    """написать валидацию на проверку имени и почты"""


class LoginForm(FlaskForm):
    username = wtforms.StringField('Имя пользователя', validators=[DataRequired('Поле не может быть пустым')])
    password = wtforms.PasswordField('Пароль', validators=[DataRequired('Поле не может быть пустым')])
    remember_me = wtforms.BooleanField('Запомнить меня')
    submit = wtforms.SubmitField('Войти')