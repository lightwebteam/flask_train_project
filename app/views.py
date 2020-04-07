from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import TestForm, Register, LoginForm
from app.models import Test_table, User
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/index', methods=['GET', 'POST'])
@login_required  # этот декоратор дополняет (login.login_view = 'login') в файле __init__
def index():
    form = TestForm()
    hello_list = [1, 2, 'str', 2.56112]
    if request.method == 'POST':
        if form.validate_on_submit():
            query_last_index = db.session.query(db.func.max(Test_table.id)).first()
            if query_last_index is None:
                new_index = 1
            else:
                new_index = query_last_index[0] + 1
            new_letter = Test_table(id=new_index, data=form.test_form.data)
            db.session.add(new_letter)
            db.session.commit()
    return render_template('index.html', any_list=hello_list, form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    elif request.method == 'POST':
        new_user = User(username=form.username.data, email=form.email.data, sex=form.sex.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        redirect(url_for('index'))
    form = LoginForm()
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        return render_template('login.html', form=form)

    if request.method == 'POST':
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        print(user)
        login_user(user)
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
