# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem import app
from vallorem.form import TypeProductionForm
from vallorem.model import db, Categorie#, TypeProduction


@app.route('/typeProduction/')
def typeProduction(action=None):
	onglet = {'typeProd': 'selected'}
	return render_template('typeProduction/typeProduction.html', page=onglet)

@app.route('/typeProduction/ajout', methods=['GET', 'POST'])
def typeProductionAjout(action=None):
    form = TypeProductionForm(request.form)
    onglet = {'typeProduction': 'selected'}

    if request.method == "POST" and form.validate_on_submit():
    #ecrire des codes pour ajouter input dans la base de donnees
        typeprod = TypeProduction(description = form.typeProduction.data)
        with db.session() as s:
            s.add(typeprod)
        #flash('vous avez entré la description:'+form.production.data)
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash("Field %s: %s" % (
                    getattr(form, field).label.text, error), category='error')
    return render_template('production/ajout.html', page=onglet, form=form)
