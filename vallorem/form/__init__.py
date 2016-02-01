# -*- coding:utf-8 -*-
from flask.ext.wtf import Form

from wtforms import TextField, BooleanField, SubmitField, TextAreaField
from wtforms import PasswordField, SelectField, DateField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import Optional, InputRequired
from wtforms.validators import DataRequired as Required

from vallorem.model import db, Categorie, Equipe, Statut, TypeProduction
from vallorem.model import Personne
from vallorem.form.fields import ToggleField, AutoFillField


class PageForm(Form):
    titre = TextField('Titre', validators=[Required()])
    categorie_id = SelectField(u'Catégorie', coerce=int)
    content = TextAreaField('Contenu', validators=[Required()])
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        with db.session() as s:
            cats = s.query(Categorie).all()
        self.categorie_id.choices = [(c.id, c.description) for c in cats]


class PersonneForm(Form):
    nom = TextField('Nom', validators=[Required()])
    prenom = TextField('Prenom', validators=[Required()])
    nom_jf = TextField('Nom de jeune fille')
    date_naissance = DateField('Date de naissance',
                                validators=[Optional()])
    date_recrutement = DateField('Date de recrutement',
             validators=[Optional()])
    statut = AutoFillField('Statut', validators=[Required()])
    equipe_id = SelectField('Equipe', coerce=int, validators=[Required()])
    permanent = ToggleField('Permanent')

    def __init__(self, *args, **kwargs):
        super(PersonneForm, self).__init__(*args, **kwargs)
        with db.session() as s:
            sts = s.query(Statut).all()
            equipes = s.query(Equipe).all()
        self.statut.choices = [s.description for s in sts]
        self.equipe_id.choices = [(e.id, e.nom) for e in equipes]

class StatutForm(Form):
    description = TextField('Nom', validators=[Required()])

class CategorieForm(Form):
    description = TextField('Description', validators=[Required()])
    submit = SubmitField('Submit')

class EquipeForm(Form):
    nom = TextField('Nom', validators=[Required()])
    axe = TextField('Axe', validators=[Required()])
    localisation = TextField('Localisation', validators=[Required()])


class UserForm(Form):
    mail = TextField('Email', validators=[Required()])
    passwd = PasswordField('Password', validators=[Optional()])
    submit = SubmitField('Submit')


class LoginForm(Form):
    email = TextField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Submit')


class ProductionForm(Form):
    titre = TextField('Titre', validators=[Required()])
    id_type = SelectField(u'Type de production', coerce=int)
    date = DateField('Date')#, format='%Y/%m/%d')
    extra = TextField('Extra', validators=[Required()])
    description = TextAreaField('Description', validators=[Required()])

    def __init__(self, *args, **kwargs):
        super(ProductionForm, self).__init__(*args, **kwargs)
        with db.session() as s:
            types = s.query(TypeProduction).all()
        self.id_type.choices = [(t.id, t.description) for t in types]


class TypeProductionForm(Form):
    description = TextField('Description', validators=[Required()])
    publication = ToggleField('Publication')


class DoctorantForm(Form):
    id_personne = SelectField("Personne", coerce=int)
    sujet_these = TextField('Sujet de these', validators=[Required()])
    type_financement = TextField('typeFinancement', validators=[Required()])
    nombre_ia = IntegerField('Nombre d\'inscription administrative',
                             validators=[InputRequired()])
    date_soutenance = DateField('Date de soutenance', validators=[Optional()])
    observation = TextAreaField('Observation', validators=[Optional()])

    def __init__(self, *args, **kwargs):
        super(DoctorantForm, self).__init__(*args, **kwargs)
        with db.session() as s:
            people = s.query(Personne).all()
        self.id_personne.choices = [(p.id, p) for p in people]


class DatePromotionForm(Form):
    id_personne = SelectField("Personne", coerce=int)
    statut = TextField('Nouveau statut', validators=[Required()])
    date_promotion = DateField('Date de promotion', validators=[Required()])

    def __init__(self, *args, **kwargs):
        super(DatePromotionForm, self).__init__(*args, **kwargs)
        with db.session() as s:
            people = s.query(Personne).all()
        self.id_personne.choices = [(p.id, p) for p in people]


class ChgEquipeForm(Form):
    equipe = TextField('Equipe', validators=[Required()])
    dateChgEquipe = DateField("Date de changement d'equipe", validators=[Required()])
