from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import (
    StringField, 
    SubmitField, 
    TextAreaField,
    SelectField,
    )

class UploadForm(FlaskForm):
    title = StringField('Title')
    body = TextAreaField('Text', render_kw={"rows": 10, "cols": 10})
    dt = StringField(validators=[DataRequired()])
    submit = SubmitField('Upload')

class TableForm(FlaskForm):
    opts = SelectField('Date', choices=[])
    submit = SubmitField('Update')

class GraphForm(FlaskForm):
    opts = SelectField('Date', choices=[])
    # chart series
    series_1 = SelectField('Bilan (1)', choices=[])
    series_2 = SelectField('Bilan (2)', choices=[])
    series_3 = SelectField('Bilan (3)', choices=[])
    # chart type
    types = [('area', 'Area'), ('line', 'Line'), ('column', 'Column')]
    type_1 = SelectField('Series 1', choices=types, default='area')
    type_2 = SelectField('Series 2', choices=types, default='line')
    type_3 = SelectField('Series 3', choices=types, default='column')

    submit1 = SubmitField('Update')
    submit2 = SubmitField('Update')