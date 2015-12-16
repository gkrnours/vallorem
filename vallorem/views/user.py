# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import request, session, redirect, url_for, flash
from flask import render_template
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError

from vallorem import app
from vallorem.model import db, Mail

# local import
from vallorem.model.user import User
from vallorem.form import UserForm
from vallorem import app

@app.route('/user/')
def user(action=None):
    ctx = {}
    with db.session() as s:
        ctx['users'] = s.query(User).all()
    ctx['page'] = {'user': 'selected'}
    return render_template('user/user.html', **ctx)


@app.route('/user/ajout', methods=['GET', 'POST'])
def userAjout():
    form=UserForm(request.form)
    onglet = {'user': 'selected'}
    if request.method == "POST" and form.validate():
        with db.session() as s:
            mail = s.query(Mail).filter(Mail.mail == form.email.data).first()
        if mail is None:
            mail = Mail(mail=form.email.data)
        user = User(mail=mail, password=form.password.data)
        try:
            with db.session() as s:
                if inspect(mail).transient:
                    s.add(mail)
                s.add(user)
        except IntegrityError:
            flash("Le mail déjà existant ", category="error")
            return render_template('user/ajout.html',form=form, page=onglet)
        flash("vous avez créé un compte avec l'email: %s" %form.email.data,category='success')
        return redirect(url_for('user'))

    return render_template('user/ajout.html',form=form, page=onglet)

@app.route('/user/modif', methods=['GET', 'POST'])
def userModif():
    onglet = {'user': 'selected'}
    return render_template('user/ajout.html', page=onglet)

@app.route('/user/delete')
@app.route('/user/delete/<id>')
def userDelete(id):

    with db.session() as s:
        s.query(User).filter(User.id == id).delete()
    return redirect(url_for('user'))