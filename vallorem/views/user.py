# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem.form import UserForm
from vallorem import app

@app.route('/user/')
def user(action=None):
    onglet = {'user': 'selected'}
    return render_template('user/user.html', page=onglet)


@app.route('/user/ajout', methods=['GET', 'POST'])
def userAjout():
    form=UserForm()
    onglet = {'user': 'selected'}
    if request.method == "POST":
    #ecrire des codes pour ajouter input dans la base de donnees
        form = UserForm(request.form)
        flash("vous avez entré l'email:"+form.email.data)
        flash("vous avez entré le password:"+form.password.data)

    return render_template('user/ajout.html',form=form, page=onglet)

@app.route('/user/modif', methods=['GET', 'POST'])
def userModif():
    onglet = {'user': 'selected'}
    return render_template('user/ajout.html', page=onglet)
