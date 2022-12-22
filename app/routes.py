from flask import render_template, flash, redirect, url_for, request
from app import app
from wtforms import BooleanField
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app.form import LoginForm,  ComplementaryForm, ArterialTensionForm, DonorForm, VisionForm, MedicCheckForm,  IncidentsForm, PsicologicalForm, BodyExamnForm, VacunationForm,GeneticsRisksForm, ExpositionRisksForm, CronicsIlnessForm, InitialSanitaryControlForm, PathologicalHistoryForm, InitialHealthStateForm, OcupationalHistoryForm, ResumeForm, PatienteForm, ChargesheetForm, ResetPasswordForm, ResetPasswordRequestForm
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

@app.route('/pathHist/new',methods=['GET', 'POST'])
def pathHist_new():
    if(request.method == 'POST'):
        print(request.form)
    form = PathologicalHistoryForm()
    return render_template('patiente_form.html', title='Añadir Pahtologia', form=form)

@app.route('/iSanitCont/new',methods=['GET', 'POST'])
def iniSanCon_new():
    if(request.method == 'POST'):
        print(request.form)
    form = InitialSanitaryControlForm()
    return render_template('patiente_form.html', title='Añadir Control Sanitario Inicial', form=form)

@app.route('/vacunation/new',methods=['GET', 'POST'])
def vacunations_new():
    if(request.method == 'POST'):
        print(request.form)
    form = VacunationForm()
    return render_template('patiente_form.html', title='Añadir Vacunacion', form=form)

@app.route('/geneticsrisks/new', methods=['GET', 'POST'])
def genetics_risks_new():
    if request.method == 'POST':
        print(request.form)
    form = GeneticsRisksForm()
    return render_template('patiente_form.html', title='Añadir Riesgos Genéticos', form=form)

@app.route('/exposition_risks/new', methods=['GET', 'POST'])
def exposition_risks_new():
    if request.method == 'POST':
        print(request.form)
    form = ExpositionRisksForm()
    return render_template('patiente_form.html', title='Añadir Riesgos de Exposición', form=form)

@app.route('/cronics_illness/new', methods=['GET', 'POST'])
def cronics_illness_new():
    if request.method == 'POST':
        print(request.form)
    form = CronicsIlnessForm()
    return render_template('patiente_form.html', title='Añadir Enfermedad Crónica', form=form)

@app.route('/incidents/new', methods=['GET', 'POST'])
def incidents_new():
    if request.method == 'POST':
        print(request.form)
    form = IncidentsForm()
    return render_template('patiente_form.html', title='Añadir Incidente', form=form)

@app.route('/psychological/new', methods=['GET', 'POST'])
def psychological_new():
    if request.method == 'POST':
        print(request.form)
    form = PsicologicalForm()
    return render_template('patiente_form.html', title='Añadir Evaluación Psicológica', form=form)

@app.route('/body_exam/new', methods=['GET', 'POST'])
def body_exam_new():
    if request.method == 'POST':
        print(request.form)
    form = BodyExamnForm()
    return render_template('patiente_form.html', title='Añadir Examen Físico', form=form)   

@app.route('/complementary/new', methods=['GET', 'POST'])
def complementary_new():
    if request.method == 'POST':
        print(request.form)
    form = ComplementaryForm()
    return render_template('patiente_form.html', title='Añadir Exámenes Complementarios', form=form)

@app.route('/arterial_tension/new', methods=['GET', 'POST'])
def arterial_tension_new():
    if request.method == 'POST':
        print(request.form)
    form = ArterialTensionForm()
    return render_template('patiente_form.html', title='Añadir Tensión Arterial', form=form)

@app.route('/donor/new', methods=['GET', 'POST'])
def donor_new():
    if request.method == 'POST':
        print(request.form)
    form = DonorForm()
    return render_template('patiente_form.html', title='Añadir Donación de Sangre', form=form)

@app.route('/vision/new', methods=['GET', 'POST'])
def vision_new():
    if request.method == 'POST':
        print(request.form)
    form = VisionForm()
    return render_template('patiente_form.html', title='Añadir Examen de Visión', form=form)

@app.route('/medic_check/new', methods=['GET', 'POST'])
def medic_check_new():
    if request.method == 'POST':
        print(request.form)
    form = MedicCheckForm()
    return render_template('patiente_form.html', title='Añadir Revisión Médica', form=form)

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
