from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class UsersForm(FlaskForm):
	first_name = StringField('First Name', validtors=[DataRequired()])
	age = IntegerField('Age', validators=[DataRequired()])
	submit = SubmitField('Enter')

	