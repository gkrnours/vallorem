# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem.form import CategorieForm
from sqlalchemy import Table, create_engine, MetaData
from vallorem.model.categorie import Categorie
from vallorem import app
from vallorem.model import db, Categorie

from flask.ext.sqlalchemy import SQLAlchemy

@app.route('/typeProduction/')
def typeProduction(action=None):
	onglet = {'typeProd': 'selected'}
	return render_template('typeProduction/typeProduction.html', page=onglet)

@app.route('/typeProduction/ajout')
def typeProductionAjout(action=None):
    return "ajout"
