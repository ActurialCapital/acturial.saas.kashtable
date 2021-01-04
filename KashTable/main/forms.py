from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import (StringField, 
                     SubmitField, 
                     SelectField,
                     DateField)


class UploadAdminForm(FlaskForm):
    opts = SelectField('User', choices=[], validators=[DataRequired()])
    dt = DateField('Date', validators=[DataRequired()])
    name = StringField('File Name', validators=[DataRequired()])
    submit = SubmitField('Upload')
