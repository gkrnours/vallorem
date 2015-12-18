# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem import app
from vallorem.form import DatePromotionForm
from vallorem.model import db, DatePromotion

@app.route('/datePromotion/')
def datePromotion(action=None):
    onglet = {'datePromotion': 'selected'}
    return render_template('datePromotion/datePromotion.html', page=onglet)

@app.route('/datePromotion/ajout', methods=['GET', 'POST'])
def datePromotionAjout(action=None):
    form = DatePromotionForm(request.form)
    onglet = {'datePromotion': 'selected'}

    if request.method == "POST" and form.validate_on_submit():
    #ecrire des codes pour ajouter input dans la base de donnees
        dateProd = DatePromotion(description = form.datePromotion.data)
        with db.session() as s:
            s.add(dateProd)
        #flash('vous avez entré la description:'+form.production.data)
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash("Field %s: %s" % (
                    getattr(form, field).label.text, error), category='error')
    return render_template('datePromotion/ajout.html', page=onglet, form=form)
