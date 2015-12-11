from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired as Required
from vallorem.model import Categorie


class PageForm(Form):
<<<<<<< HEAD
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
=======
    title = TextField('title', validators=[Required()])
    categories = []
#    categories = Categorie.query.all()
    choices = []
    for categ in categories:
        choices.append((getattr(categ, "id"), getattr(categ, "description")))

    categorie = SelectField(u'Categorie', choices=choices)
    contenu = TextAreaField('contenu', validators=[Required()])
    submit = SubmitField('Submit')


class CategorieForm(Form):
    description = TextField('description', validators=[Required()])
    submit = SubmitField('Submit')


class UserForm(Form):
    email = TextField('email', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
    submit = SubmitField('Submit')
>>>>>>> 5d41e10955468e5c91f860e5c5e658c78d2dd7cd


class LoginForm(Form):
    username = TextField('username', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
    submit = SubmitField('Submit')
