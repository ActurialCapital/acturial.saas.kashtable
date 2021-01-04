from flask_wtf import FlaskForm
from wtforms import SubmitField

class RedirectHomeForm(FlaskForm):
    submit = SubmitField('Return Home')
