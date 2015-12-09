# -*- encoding: utf-8 -*-

import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort
from flask import render_template, flash, redirect
import click
from contextlib import closing
from form import PageForm,CategorieForm
from vallorem import app

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    return rv


def init_db():
    """Initializes the database."""
    with closing(connect_db()) as db:
        with app.open_resource('vallorem.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@click.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.route('/')
def home():
    return redirect('index')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/config')
@app.route('/config/<action>')
def config(action = None):
    onglet = {'sys': 'selected'}
    if(action==None):
        return render_template('page.html', page=onglet)
    else:
        return "Action non valide"

@app.route('/page/')
@app.route('/page/<action>', methods=['GET', 'POST'])
def page(action=None):

    form=PageForm()
    onglet = {'sys': 'selected'}
    
    if(action == None):     
        return render_template('page.html', page=onglet)
    elif(action == "ajout"):
        if request.method == "POST":
         #ecrire des codes pour ajouter input dans la base de donnees
            form = PageForm(request.form)
        return render_template('page/ajout.html', page=onglet, form=form)
    elif(action == "modif"):
        if request.method == "POST":
         #ecrire des codes pour ajouter input dans la base de donnees
            form = PageForm(request.form)
        return render_template('page/ajout.html', page=onglet, form=form)
        
    else:
        return "Action non valide"
81

@app.route('/categorie/')
@app.route('/categorie/<action>', methods=['GET', 'POST'])
def categorie(action=None):

    onglet = {'categ': 'selected'}
    form=CategorieForm()
    
    if(action == None):
        return render_template('categorie.html', page=onglet)
    elif(action == "ajout"):
        if request.method == "POST":
         #ecrire des codes pour ajouter input dans la base de donnees
            form = CategorieForm(request.form)
        return render_template('categorie/ajout.html', page=onglet ,form=form)
    elif(action == "modif"):
        if request.method == "POST":
         #ecrire des codes pour ajouter input dans la base de donnees
            form = CategorieForm(request.form)
        return render_template('categorie/ajout.html', page=onglet ,form=form)
        
    else:
        return "Action non valide"

@app.route('/user/')
@app.route('/user/<action>')
def user(action=None):
    onglet = {'user': 'selected'}
    if(action == None):
        return render_template('user.html', page=onglet)
    elif(action == "ajout"):
        return render_template('user/ajout.html', page=onglet)
    elif(action == "modif"):
        return render_template('user/ajout.html', page=onglet)
    else:
        return "Action non valide"



