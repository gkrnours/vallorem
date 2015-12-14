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

@app.route('/personne/')
def personne(action=None):
    onglet = {'personne': 'selected'}
    return render_template('personne/personne.html', page=onglet)

@app.route('/personne/ajout')
def personneAjout(action=None):
    return "personne"
