from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SubmitField, TextAreaField,PasswordField, SelectField
from wtforms.validators import DataRequired as Required

class PageForm(Form):
	title= TextField('Title', validators=[Required()])
	categorie = SelectField(u'Categorie', choices=[('1', 'test'), ('2', 'test2'), ('3', 'test3'),('3', 'test3'),('4', 'test4')])
	contenu=TextAreaField('Contenu', validators=[Required()])
	submit = SubmitField('Submit')
	
class CategorieForm(Form):
	description= TextField('Description', validators=[Required()])
	submit = SubmitField('Submit')

class UserForm(Form):
	email= TextField('Email', validators=[Required()])
	password= PasswordField('Password', validators=[Required()])
	submit = SubmitField('Submit')

class LoginForm(Form):
	username= TextField('Username', validators=[Required()])
	password= PasswordField('Password', validators=[Required()])
	submit = SubmitField('Submit')


