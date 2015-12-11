# -*- encoding: utf-8 -*-
# std python importCategorie.query.all
from __future__ import unicode_literals
from vallorem.model import db

# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem.model.db import engine
from vallorem.form import PageForm
from vallorem.model.page import Page
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from vallorem import app

@app.route('/page/')
def page(action=None):
    pages = Page.query.all()
    pageTab = {}
    for page in pages:
        pageTab.update({getattr(page, "id") : getattr(page, "titre")})
    onglet = {'sys': 'selected'}
    form=PageForm() 
    return render_template('page/page.html', page=onglet, pageData = pageTab)

@app.route('/page/ajout', methods=['GET', 'POST'])
def pageAjout():
    onglet = {'sys': 'selected'}
    form=PageForm()
    if request.method == "POST":
    #ecrire des codes pour ajouter input dans la base de donnees
        form = PageForm(request.form)
        flash('vous avez entré le title:'+form.title.data)
        flash('vous avez entré la categorie:'+form.categorie.data, 'success')
        flash('vous avez entré le contenu:'+form.contenu.data, 'info')
    return render_template('page/ajout.html', page=onglet, form=form)

@app.route('/page/modif', methods=['GET', 'POST'])
def pageModif():
    form=PageForm()
    onglet = {'sys': 'selected'}
    if request.method == "POST":
    #ecrire des codes pour ajouter input dans la base de donnees
        form = PageForm(request.form)
    return render_template('page/ajout.html', page=onglet, form=form)

@app.route('/page/delete')
@app.route('/page/delete/<id>')
def pageDelete(id):

    with db.session() as s:
        Page.query.filter(Page.id == id).delete()
    return redirect(url_for('page'))