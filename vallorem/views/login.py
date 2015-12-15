# -*- encoding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import request, session, redirect, url_for, flash
from flask import render_template as render
from flask.ext.login import login_user, logout_user
# local import
from vallorem.form import LoginForm
from vallorem.model import db,Mail,User
from vallorem import app




@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        with db.session() as s:
            mail = s.query(Mail).filter(Mail.mail == form.email.data).first()
            if mail is None:
                pass
            user = s.query(User).filter(User._mail == mail).first()
        if user is not None and user.password==form.password.data:
            login_user(user)
            return redirect(request.args.get('next') or url_for('index'))
        flash('invalide username or password', category="error")
    elif request.method == "POST":
        flash("\n".join(form.errors), category="error")
    return render('login.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('home'))
