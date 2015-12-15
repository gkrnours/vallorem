# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem.form import CategorieForm,PersonneForm
from vallorem import app
from vallorem.model import db, Categorie, Personne,Statut

from flask.ext.sqlalchemy import SQLAlchemy

@app.route('/personne/')
def personne(action=None):
    onglet = {'personne': 'selected'}
    with db.session() as s:
        p = s.query(Personne).all()
    return render_template('personne/personne.html', page=onglet, personnes=p)

@app.route('/personne/ajout', methods=['GET', 'POST'])
def personneAjout(action=None):
    onglet = {'personne': 'selected'}
    form = PersonneForm(request.form)
    if request.method == "POST" and form.validate():
        with db.session() as s:
            statut = s.query(Statut).filter(Statut.description == form.statut.data).first()
        if statut is None:
            statut = Statut(description=form.statut.data)
        data = {f.short_name: f.data for f in form}
        data['statut'] = statut
        del data['csrf_token']
        p = Personne(**data)
        with db.session() as s:
            s.add(statut)
            s.add(p)
        flash("vous avez créé une personnage avec le nom et le prenom: %s , %s" %(form.nom.data, form.prenom.data), category='success')
        return redirect(url_for('personne'))
    elif app.config['DEBUG'] and request.method == "POST":
        flash('\n'.join(form.errors), category='error')
    return render_template('personne/ajout.html',form=form, page=onglet)


