from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SubmitField, TextAreaField, PasswordField, SelectField, DateField, IntegerField
from wtforms.validators import DataRequired as Required
from vallorem.model import db, Categorie, Observation, Personne, TypeFinancement


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


class CategorieForm(Form):
    description= TextField('Description', validators=[Required()])
    submit = SubmitField('Submit')


class UserForm(Form):
    email= TextField('Email', validators=[Required()])
    password= PasswordField('Password', validators=[Required()])
    submit = SubmitField('Submit')


class LoginForm(Form):
	email= TextField('email', validators=[Required()])
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


class DoctorantForm(Form):

    sujetThese = TextField('Sujet de these', validators=[Required()])
    typeFinancement = SelectField(u'typeFinancement', coerce=int)
    personne = SelectField(u'personne', coerce=int)
    observation = TextField('Observation', validators=[Required()])
    nbInscription = IntegerField('Nombre d\'inscription administrative', validators=[Required()])

    dateSoutenance = DateField('Date de soutenance', format='%d/%m/%Y')

    def __init__(self, *args, **kwargs):
        super(DoctorantForm, self).__init__(*args, **kwargs)
        with db.session() as s:
            typeFinancements = s.query(TypeFinancement).all()
            self.typeFinancement.choices = [(c.id, c.description) for c in typeFinancements]

            personnes = s.query(Personne).all()
            self.personne.choices = [(c.id, c.description) for c in personnes]




