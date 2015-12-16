# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem.form import DoctorantForm, PersonneForm
from vallorem import app
from vallorem.model import db, Categorie, Personne, Doctorant, Statut, Observation, TypeFinancement

from flask.ext.sqlalchemy import SQLAlchemy

@app.route('/doctorant/')
def doctorant(action=None):
    onglet = {'doctorant': 'selected'}
    with db.session() as s:
        d = s.query(Doctorant).all()
    return render_template('doctorant/doctorant.html', page=onglet, doctorants=d)

@app.route('/doctorant/ajout', methods=['GET', 'POST'])
def doctorantAjout(action=None):
    form = DoctorantForm(request.form)
    formP = PersonneForm(request.form)
    onglet = {'doctorant': 'selected'}
    if request.method == "POST" and form.validate():
        with db.session() as s:
            statut = s.query(Statut).filter(Statut.description == formP.statut.data).first()

            observation = s.query(Observation).filter(Observation.description == form.observation.data).first()

            typeFinancement = s.query(TypeFinancement).filter(TypeFinancement.description == form.type_financement.data).first()
        if statut is None:
            statut = Statut(description=formP.statut.data)
        if observation is None:
            observation = Observation(description=form.observation.data)
        if typeFinancement is None:
            typeFinancement = TypeFinancement(description=form.type_financement.data)
        data = {f.short_name: f.data for f in form}
        dataP = {f.short_name: f.data for f in formP}
        del data['csrf_token']
        del dataP['csrf_token']
        dataP['statut'] = statut
        data['type_financement'] = typeFinancement
        data['observation'] = observation
        from pprint import pprint
        pprint(data)
        p = Personne(**dataP)
        d = Doctorant(**data)
        d.personne=p
        d.type_financement = typeFinancement
        pprint(dataP)
        pprint(p)

        with db.session() as s:
            s.add(statut)
            s.add(p)
            s.add(typeFinancement)
            s.add(observation)
            s.add(d)

        flash("vous avez créé le doctorant %s %s" 
            %(formP.nom.data, formP.prenom.data), category='success')
        return redirect(url_for('doctorant'))

    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash("Field %s: %s" % (
                    getattr(form, field).label.text, error), category='error')
    return render_template('doctorant/ajout.html', page=onglet, form=form, formP=formP)



    