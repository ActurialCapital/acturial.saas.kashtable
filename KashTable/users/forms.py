from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from wtforms import (
    StringField, 
    PasswordField, 
    SubmitField, 
    BooleanField,
    RadioField,
    TextAreaField,
    SelectField
    )
from KashTable.models import User


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])    
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    company_name = StringField('Company Name', validators=[DataRequired(), Length(min=2, max=20)])      
    street = StringField('Street', validators=[DataRequired(), Length(min=2, max=20)])     
    postcode = StringField('Postcode', validators=[DataRequired(), Length(min=2, max=20)])      
    city = StringField('City', validators=[DataRequired(), Length(min=2, max=20)])    
    country = StringField('Country', validators=[DataRequired(), Length(min=2, max=20)])   
    siren = StringField('Siren', validators=[DataRequired(), Length(min=2, max=20)])   
    bundle = RadioField('Select Bundle', choices=[('1','Standard'),('2','Analytics')], validators=[DataRequired()], default='2')
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])    
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    company_name = StringField('Company Name', validators=[DataRequired(), Length(min=2, max=20)])      
    street = StringField('Street', validators=[DataRequired(), Length(min=2, max=20)])     
    postcode = StringField('Postcode', validators=[DataRequired(), Length(min=2, max=20)])      
    city = StringField('City', validators=[DataRequired(), Length(min=2, max=20)])    
    country = StringField('Country', validators=[DataRequired(), Length(min=2, max=20)])   
    siren = StringField('Siren', validators=[DataRequired(), Length(min=2, max=20)])   
    bundle = RadioField('Select Bundle', choices=[('1','Standard'),('2','Analytics')], validators=[DataRequired()], default='2')
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choo se a different one.')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
    
    
class UploadForm(FlaskForm):
    title = StringField('Title')
    body = TextAreaField('Text', render_kw={"rows": 10, "cols": 10})
    dt = StringField(validators=[DataRequired()])
    submit = SubmitField('Upload')

class TableForm(FlaskForm):
    opts = SelectField('Date', choices=[])
    submit = SubmitField('Update')
