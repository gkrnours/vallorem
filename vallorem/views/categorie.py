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

@app.route('/categorie/')
@app.route('/categorie/<action>', methods=['GET', 'POST'])
def categorie(action=None):


    categories = Categorie.query.all()
    categDescri = []
    for categ in categories:
        categDescri.append(getattr(categ, "description"))
    onglet = {'categ': 'selected'}
    form=CategorieForm()
    return render_template('categorie/categorie.html', page=onglet, categ=categDescri)
    

@app.route('/categorie/ajout', methods=['GET', 'POST'])
def categorieAjout():
    form=CategorieForm()
    onglet = {'categ': 'selected'}
    if request.method == "POST":
    #ecrire des codes pour ajouter input dans la base de donnees
        form = CategorieForm(request.form)
        flash('vous avez entré la description:'+form.description.data)
    return render_template('categorie/ajout.html', page=onglet, form=form)

@app.route('/categorie/modif', methods=['GET', 'POST'])
def categorieModif():
    form=CategorieForm()
    onglet = {'categ': 'selected'}
    if request.method == "POST":
    #ecrire des codes pour ajouter input dans la base de donnees
        form = CategorieForm(request.form)
    return render_template('categorie/ajout.html', page=onglet, form=form)
