from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import (
    StringField, 
    SubmitField, 
    TextAreaField,
    SelectField
    )

class UploadForm(FlaskForm):
    title = StringField('Title')
    body = TextAreaField('Text', render_kw={"rows": 10, "cols": 10})
    dt = StringField(validators=[DataRequired()])
    submit = SubmitField('Upload')

class TableForm(FlaskForm):
    opts = SelectField('Date', choices=[])
    submit = SubmitField('Update')
