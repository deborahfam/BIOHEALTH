from flask import render_template, flash, redirect, url_for, request
from app import app
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app.form import LoginForm, InitialHealthStateForm, OcupationalHistoryForm, ResumeForm, PatienteForm, ChargesheetForm, ResetPasswordForm, ResetPasswordRequestForm
from app.email import send_password_reset_email

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': current_user.username}
    return render_template('index.html', title =' Home', user=user)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/patiente/new',methods=['GET', 'POST'])
def user_new():
    if(request.method == 'POST'):
        print(request.form)
    form = PatienteForm()
    return render_template('patiente_form.html', title='Añadir Paciente', form=form)

@app.route('/chargesheet/new',methods=['GET', 'POST'])
def chargeheet_new():
    if(request.method == 'POST'):
        print(request.form)
    form = ChargesheetForm()
    return render_template('patiente_form.html', title='Añadir Hoja de Cargo', form=form)

@app.route('/resume/new',methods=['GET', 'POST'])
def resume_new():
    if(request.method == 'POST'):
        print(request.form)
    form = ResumeForm()
    return render_template('patiente_form.html', title='Añadir Resumen', form=form)

@app.route('/histOcup/new',methods=['GET', 'POST'])
def histOcup_new():
    if(request.method == 'POST'):
        print(request.form)
    form = OcupationalHistoryForm()
    return render_template('patiente_form.html', title='Añadir Historia Ocupacional', form=form)

@app.route('/ihs/new',methods=['GET', 'POST'])
def inihealthstate_new():
    if(request.method == 'POST'):
        print(request.form)
    form = InitialHealthStateForm()
    return render_template('patiente_form.html', title='Añadir Resumen', form=form)


# @app.route('/reset_password_request', methods=['GET', 'POST'])
# def reset_password_request():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = ResetPasswordRequestForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user:
#             send_password_reset_email(user)
#         flash('Check your email for the instructions to reset your password')
#         return redirect(url_for('login'))
#     return render_template('reset_password_request.html',
#                            title='Reset Password', form=form)


# @app.route('/reset_password/<token>', methods=['GET', 'POST'])
# def reset_password(token):
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     user = User.verify_reset_password_token(token)
#     if not user:
#         return redirect(url_for('index'))
#     form = ResetPasswordForm()
#     if form.validate_on_submit():
#         user.set_password(form.password.data)
#         db.session.commit()
#         flash('Your password has been reset.')
#         return redirect(url_for('login'))
#     return render_template('reset_password.html', form=form)
