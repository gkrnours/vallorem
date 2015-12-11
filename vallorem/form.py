from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SubmitField, TextAreaField,PasswordField, SelectField
from wtforms.validators import DataRequired as Required
from vallorem.model.db import engine
from vallorem.model.categorie import Categorie

class PageForm(Form):
	title= TextField('title', validators=[Required()])
	categories = Categorie.query.all()
	choices = []
	for categ in categories:
		choices.append((getattr(categ, "id"),getattr(categ, "description")))

	categorie = SelectField(u'Categorie', choices=choices)
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


