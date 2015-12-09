from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SubmitField, TextAreaField,PasswordField
from wtforms.validators import DataRequired as Required

class PageForm(Form):
	title= TextField('title', validators=[Required()])
	categorie=TextField('categorie', validators=[Required()])
	contenu=TextAreaField('contenu', validators=[Required()])
	submit = SubmitField('Submit')
	
class CategorieForm(Form):
	description= TextField('description', validators=[Required()])
	submit = SubmitField('Submit')

class UserForm(Form):
	email= TextField('email', validators=[Required()])
	password= PasswordField('password', validators=[Required()])
	submit = SubmitField('Submit')

class LoginForm(Form):
	username= TextField('username', validators=[Required()])
	password= PasswordField('password', validators=[Required()])
	submit = SubmitField('Submit')


