from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired as Required

class PageForm(Form):
	title= TextField('title', validators=[Required()])
	categorie=TextField('categorie', validators=[Required()])
	contenu=TextAreaField('contenu', validators=[Required()])
	submit = SubmitField('Submit')
	
class CategorieForm(Form):
	description= TextField('description', validators=[Required()])
	submit = SubmitField('Submit')
