from flask_wtf import FlaskForm as Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class ContentForm(Form):
    description = StringField('description', validators=[DataRequired()])
    gender = SelectField('Gender', default='Female', choices=[
        ('female', 'Femme'),
        ('male', 'Homme'),
        ('other', 'Non défini')
    ])
