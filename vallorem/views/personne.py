# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem.form import CategorieForm,PersonneForm, DatePromotionForm
from vallorem import app
from vallorem.model import db, Categorie, Personne,Statut,Equipe,DatePromotion

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



@app.route('/personne/info/<int:personne_id>')
def personneInfo(personne_id):
    onglet = {'personne': 'selected'}
    with db.session() as s:
        p = s.query(Personne).filter(Personne.id==personne_id).first()
    return render_template('personne/personneInfo.html', page=onglet, personne=p, personne_id=personne_id)


@app.route('/personne/modif/<int:personne_id>', methods=['GET', 'POST'])
def personneModifierStatus(personne_id):
    onglet = {'status': 'selected'}
    form = DatePromotionForm(request.form)

    if request.method == "POST" and form.validate():
        with db.session() as s:
            status=s.query(Statut).filter(Statut.description==form.statut.data).first()
            if status is None:
                status=Statut(description=form.statut.data)
                s.add(status)
            promotion=DatePromotion(id_personne=personne_id, id_statut=status.id, date_promotion=form.datePromotion.data)
            s.add(promotion)
            flash("vous avez changé le status: %s , %s" %(form.statut.data, promotion), category='success')
            return redirect(url_for('personneInfo', personne_id=personne_id))
    elif app.config['DEBUG'] and request.method == "POST":
        flash('\n'.join(form.errors), category='error')
    else:
        flash(request.method)

    return render_template('personne/ajoutStatus.html', form=form, page=onglet, personne_id=personne_id)