# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem.form import CategorieForm
from vallorem import app
from vallorem.model import db, Categorie

from flask.ext.sqlalchemy import SQLAlchemy

@app.route('/statut/')
def statut(action=None):
    onglet = {'statut': 'selected'}
    return render_template('statut/statut.html', page=onglet)

@app.route('/statut/ajout')
def statutAjout(action=None):
    return "statut"
