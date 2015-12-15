from flask.ext.wtf import Form

from wtforms import TextField, BooleanField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.fields.html5 import DateField

from wtforms.validators import DataRequired as Required
from vallorem.model import db, Categorie


class PageForm(Form):
    title= TextField('Title', validators=[Required()])
    categorie = SelectField(u'Categorie', coerce=int)
    contenu=TextAreaField('Contenu', validators=[Required()])
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        with db.session() as s:
            cats = s.query(Categorie).all()
            self.categorie.choices = [(c.id, c.description) for c in cats]


class PersonneForm(Form):
    nom = TextField('Nom', validators=[Required()])
    prenom = TextField('Prenom', validators=[Required()])
    nom_jf = TextField('Nom de jeune fille')
    date_naissance = DateField('Date de naissance', validators=[Required()])
    date_recrutement = DateField('Date de recrutement', validators=[Required()])
    statut = TextField('Statut', validators=[Required()])
    permanent = BooleanField('Permanent')


class CategorieForm(Form):
    description= TextField('Description', validators=[Required()])
    submit = SubmitField('Submit')


class UserForm(Form):
    email= TextField('Email', validators=[Required()])
    password= PasswordField('Password', validators=[Required()])
    submit = SubmitField('Submit')


class LoginForm(Form):
	email= TextField('Email', validators=[Required()])
	password= PasswordField('Password', validators=[Required()])
	submit = SubmitField('Submit')



class ProductionForm(Form):
    titre = TextField('Titre', validators=[Required()])
    description = TextField('Description', validators=[Required()])
    extra = TextField('Extra', validators=[Required()])
    date = DateField('Date', format='%d/%m/%Y')

class TypeProductionForm(Form):

    description = TextField('Description', validators=[Required()])
    publication = BooleanField('Publication')

