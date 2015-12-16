# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem import app
from vallorem.model import db
from vallorem.form import ProductionForm
from flask.ext.sqlalchemy import SQLAlchemy

@app.route('/production/')
def production(action=None):
    onglet = {'prod': 'selected'}
    return render_template('production/production.html', page=onglet)

@app.route('/production/ajout', methods=['GET', 'POST'])
def productionAjout(action=None):
    form = ProductionForm(request.form)
    onglet = {'production': 'selected'}

    if request.method == "POST" and form.validate_on_submit():
    #ecrire des codes pour ajouter input dans la base de donnees
        prod = Production(description = form.description.data)
        with db.session() as s:
            s.add(prod)
        #flash('vous avez entré la description:'+form.production.data)
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash("Field %s: %s" % (
                    getattr(form, field).label.text, error), category='error')
    return render_template('production/ajout.html', page=onglet, form=form)