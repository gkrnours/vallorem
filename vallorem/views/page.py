# -*- encoding: utf-8 -*-

# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem.form import PageForm
from vallorem import app

@app.route('/page/')
def page(action=None):
    onglet = {'sys': 'selected'}
    form=PageForm()
    onglet = {'sys': 'selected'}   
    return render_template('page/page.html', page=onglet)

@app.route('/page/ajout', methods=['GET', 'POST'])
def pageAjout():
    onglet = {'sys': 'selected'}
    form=PageForm()
    if request.method == "POST":
    #ecrire des codes pour ajouter input dans la base de donnees
        form = PageForm(request.form)
    return render_template('page/ajout.html', page=onglet, form=form)

@app.route('/page/modif', methods=['GET', 'POST'])
def pageModif():
    form=PageForm()
    onglet = {'sys': 'selected'}
    if request.method == "POST":
    #ecrire des codes pour ajouter input dans la base de donnees
        form = PageForm(request.form)
    return render_template('page/ajout.html', page=onglet, form=form)