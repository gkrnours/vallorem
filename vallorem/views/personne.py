# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
from sqlalchemy import exc
# local import
from vallorem import app
from vallorem.views import utils
from vallorem.model import db, Personne, Statut, Equipe, DatePromotion
from vallorem.model import ChgEquipe
from vallorem.form import PersonneForm, DatePromotionForm, ChgEquipeForm
from vallorem.form import StatutForm, EquipeForm

# Personne

def pers_update(form, pers):
    form.populate_obj(pers)
    st = pers._statut
    if st is not None:
        pers.statut_id = st.id
        del pers._statut
    try:
        with db.session() as s:
            s.add(pers)
        flash('La personne «%s» a été modifiée.' % pers)
        return True
    except exc.IntegrityError as e:
        print(e)
        flash('Les données saisies sont invalide.', category='failure')
        return False

utils.make_crud(
    app, Personne, PersonneForm,
    {'name': 'personne', 'path':'/personne/', 'tpl':'personnel/personne/'},
    _update=pers_update,
    msg = {
        'delete': 'La personne «%s» a été supprimée.',
        'insert': {
            'success': 'La personne «%s» a été ajoutée.',
            'failure': 'Les données saisies sont invalide.'
        },
    }
)

@app.route('/personne/info/<int:id>')
def personneInfo(id):
    with db.session() as s:
        p = s.query(Personne).get(id)
    return render_template('personnel/personne/info.html', personne=p)

# Statut

def statut_insert(form):
    statut = Statut(form.description.data)
    try:
        with db.session() as s:
            s.add(statut)
        flash('Le statut «%s» a été ajouté.' % statut, category="success")
        return True
    except exc.IntegrityError:
        flash('Les données saisies sont invalide.', category="danger")
        return False

utils.make_crud(
    app, Statut, StatutForm,
    {'name': 'statut', 'path':'/statut/', 'tpl':'personnel/statut/'},
    statut_insert,
    msg = {
        'delete': 'Le statut «%s» a été supprimé.',
        'update': {
            'success': 'Le statut «%s» a été modifié.',
            'failure': 'Les données saisies sont invalide.'
        }
    }
)

# Equipe

utils.make_crud(
    app, Equipe, EquipeForm,
    {'name': 'equipe', 'path':'/equipe/', 'tpl':'personnel/equipe/'},
    msg = {
        'delete': "L'équipe «%s» a été supprimé.",
        'insert': {
            'success': "L'équipe «%s» a été ajoutée.",
            'failure': 'Les données saisies sont invalide.'
        },
        'update': {
            'success': "L'équipe «%s» a été modifiée.",
            'failure': 'Les données saisies sont invalide.'
        }
    }
)
