# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import request, session, redirect, url_for, flash
from flask import render_template
from sqlalchemy import exc
# local import
from vallorem import app
from vallorem.form import UserForm
from vallorem.model import db, Mail, User
from vallorem.views import utils

def user_insert(form):
    if form.passwd.data is None:
        flash("Un mot de passe est requis.", category="danger")
        return False
    mail = Mail.get_or_create(form.mail.data)
    user = User(mail=mail, password=form.passwd.data)
    try:
        with db.session() as s:
            s.add(user)
        flash("L'utilisateur %s a été ajouté." % mail.mail, category='success')
        return True
    except exc.IntegrityError:
        flash("Les données saisies sont invalides.", category='danger')
        return False

def user_update(form, user):
    if user.mail != form.mail.data:
        user.mail = Mail.get_or_create(form.mail.data)
    if form.passwd.data is not None:
        user.password = form.passwd.data
    with db.session() as s:
        s.add(user)
    flash("L'utilisateur %s a été mis à jour." % user.mail)
    return True

utils.make_crud(
    app, User, UserForm,
    {'name':'user', 'path':'/user/', 'tpl':'site/user/'},
    user_insert, user_update,
    {'delete': "L'utilisateur %s a été supprimé."}
)
