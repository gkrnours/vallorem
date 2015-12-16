from flask.ext.wtf import Form

from wtforms import TextField, BooleanField, SubmitField, TextAreaField, PasswordField, SelectField, DateField, IntegerField

from wtforms.fields.html5 import DateField

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
    date = DateField('Date', format='%Y/%m/%d')

class TypeProductionForm(Form):

    description = TextField('Description', validators=[Required()])
    publication = BooleanField('Publication')


class DoctorantForm(Form):

    sujetThese = TextField('Sujet de these', validators=[Required()])
    typeFinancement = TextField('typeFinancement', validators=[Required()])
    personne = SelectField(u'personne', coerce=int)
   
    nbInscription = IntegerField('Nombre d\'inscription administrative', validators=[Required()])
    dateSoutenance = DateField('Date de soutenance', format='%Y/%m/%d')
    observation = TextAreaField('Observation', validators=[Required()])

    def __init__(self, *args, **kwargs):
        super(DoctorantForm, self).__init__(*args, **kwargs)
        with db.session() as s:
            personnes = s.query(Personne).all()
        self.personne.choices = [(c.id, c.nom) for c in personnes]


class DatePromotionForm(Form):

    satut = TextField('statut', validators=[Required()])
    datePromotion = DateField('Date de promotion', format='%Y/%m/%d')
    personne = SelectField(u'personne', coerce=int)

    def __init__(self, *args, **kwargs):
        super(DatePromotionForm, self).__init__(*args, **kwargs)
        with db.session() as s:
            personnes = s.query(Personne).all()
        self.personne.choices = [(c.id, c.nom) for c in personnes]