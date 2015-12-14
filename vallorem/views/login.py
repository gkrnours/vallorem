# -*- encoding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template as render
# local import
from vallorem.form import LoginForm
from vallorem import app
from flask.ext.login import login_user, logout_user, login_required



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        with db.session() as s:
            mail = s.query(Mail).filter(Mail.mail == form.email.data).first()
            if mail is None:
                pass
            user = s.query(User).filter(User._mail == mail).first()
        if user is not None and user.password==form.password.data:
            login_user(user)
            return redirect(request.args.get('next') or url_for('index'))
        flash('invalide username or password')        
    return render('login.html',form=form)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home'))
