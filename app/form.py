from flask_wtf import FlaskForm
from .constants import *
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, NumberRange, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

class PatienteForm(FlaskForm):
    ci = StringField('CI', validators=[DataRequired()])
    jobRecord = StringField('Expediente Laboral', validators=[DataRequired()])
    firstName = StringField('Nombre', validators=[DataRequired()])
    lastName = StringField('Apellidos', validators=[DataRequired()])
    out = BooleanField('Baja')
    date = DateField('Fecha de Alta', format='%d/%m/%Y')
    o_category = SelectField('Categoria', choices=[(x, x) for x in OCUP_CATEGORY])
    area = SelectField("Area", choices=[(x,x) for x in AREAS_USER_FORM])
    age = IntegerField('Edad', validators=[DataRequired(),NumberRange(min=1,max=130)])
    sex = SelectField('Sexo', choices=[('M', 'M'), ('F', 'F')])
    study_level = SelectField('Nivel Educacional', choices=[('PRIMARIA', 'PRIMARIA'), ('SECUNDARIA', 'SECUNDARIA'), ('SUPERIOR', 'SUPERIOR')])
    color_skin = SelectField('Color de Piel', choices=[('BLANCO', 'BLANCO'), ('MESTIZO', 'MESTIZO'), ('NEGRO','NEGRO')])
    tel = StringField('Telefono')
    street = StringField('Calle')
    number = StringField('Numero')
    apt = StringField('Apartamento')
    between = StringField('Entrecalle')
    neighborhood = StringField('Barrio')
    province = SelectField('Provincia', choices=[(x["nombre"],x["nombre"]) for x in CUBA_INFO])
    municipality = SelectField('Municipio', choices=[(x,x) for x in CUBA_MUNICIPALITIES])
    ageGroup = StringField('Grupo Etario')
    bloodType = SelectField('Tipo de Sangre', choices=[(x,x) for x in BLOOD_TYPE])
    donor = BooleanField('Donante')
    submit = SubmitField('Crear Entrada')