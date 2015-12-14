# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
from vallorem.model import db

# local import
from vallorem.model.user import User
from vallorem.form import UserForm
from vallorem import app

@app.route('/user/')
def user(action=None):
    with db.session() as s:
        users = s.query(User).all()

    onglet = {'user': 'selected'}
    return render_template('user/user.html', page=onglet, users=users)


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

@app.route('/user/delete')
@app.route('/user/delete/<id>')
def userDelete(id):

    with db.session() as s:
        User.query.filter(User.id == id).delete()
    return redirect(url_for('user'))