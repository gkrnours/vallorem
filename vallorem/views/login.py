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
    error = None
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.form)
        flash('vous avez entré le mail:'+form.email.data)
        if request.form['email'] != app.config['USERNAME']:
            error = 'Invalid email'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render('login.html', error=error, form=form)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home'))
