# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem.form import CategorieForm
from sqlalchemy import Table, create_engine, MetaData
from vallorem.model.db import engine
from vallorem.model.categorie import Categorie
from pprint import pprint
from vallorem import app
from vallorem.model import db, Categorie

from flask.ext.sqlalchemy import SQLAlchemy

@app.route('/categorie/')
@app.route('/categorie/<action>', methods=['GET', 'POST'])
def categorie(action=None):


    categories = Categorie.query.all()
    categTab = {}
    for categ in categories:
        categTab.update({getattr(categ, "id") : getattr(categ, "description")})
    onglet = {'categ': 'selected'}
    form=CategorieForm()
    return render_template('categorie/categorie.html', page=onglet, categData=categTab)
    

@app.route('/categorie/ajout', methods=['GET', 'POST'])
def categorieAjout():
    form = CategorieForm(request.form)
    onglet = {'categ': 'selected'}

    if request.method == "POST" and form.validate_on_submit():
    #ecrire des codes pour ajouter input dans la base de donnees
        cat = Categorie(description = form.description.data)
        with db.session() as s:
            s.add(cat)
        flash('vous avez entré la description:'+form.description.data)
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash("Field %s: %s" % (
                    getattr(form, field).label.text, error), category='error')
    return render_template('categorie/ajout.html', page=onglet, form=form)

@app.route('/categorie/modif', methods=['GET', 'POST'])
def categorieModif():
    form=CategorieForm()
    onglet = {'categ': 'selected'}
    if request.method == "POST":
    #ecrire des codes pour ajouter input dans la base de donnees
        form = CategorieForm(request.form)
    return render_template('categorie/ajout.html', page=onglet, form=form)


@app.route('/categorie/delete')
@app.route('/categorie/delete/<id>')
def categorieDelete(id):

    with db.session() as s:
        Categorie.query.filter(Categorie.id == id).delete()
    return redirect(url_for('categorie'))