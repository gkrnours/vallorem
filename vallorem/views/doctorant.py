# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem.form import DoctorantForm
from vallorem import app
from vallorem.model import db, Categorie

from flask.ext.sqlalchemy import SQLAlchemy

@app.route('/doctorant/')
def doctorant(action=None):
    onglet = {'doctorant': 'selected'}
    return render_template('doctorant/doctorant.html', page=onglet)

@app.route('/doctorant/ajout', methods=['GET', 'POST'])
def doctorantAjout(action=None):
    form = DoctorantForm(request.form)
    onglet = {'doctorant': 'selected'}
    print(form)
    if request.method == "POST" and form.validate_on_submit():
    #ecrire des codes pour ajouter input dans la base de donnees
        doct = Doctorant(description = form.description.data)
        with db.session() as s:
            s.add(doct)
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash("Field %s: %s" % (
                    getattr(form, field).label.text, error), category='error')
    return render_template('doctorant/ajout.html', page=onglet, form=form)



    