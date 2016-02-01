# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
from sqlalchemy import exc
# local import
from vallorem.form import CategorieForm
from vallorem.model import db, Categorie
from vallorem.views import utils
from vallorem import app

def categorie_insert(form):
    cat = Categorie(form.description.data)
    try:
        with db.session() as s:
            s.add(cat)
        flash("La catégorie «%s» a été ajoutée." % cat, category="success")
        return True
    except exc.IntegrityError:
        flash("Les données saisies sont invalide.", category="danger")
        return False

utils.make_crud(
    app, Categorie, CategorieForm,
    {'name':'categorie', 'path':'/categorie/', 'tpl':'site/categorie/'},
    categorie_insert, None,
    {
        'delete': 'La catégorie «%s» a été supprimée',
        'update': {
            'success': "La catégorie «%s» a été modifiée.",
            'failure': "Les données saisies sont invalide.",
        },
    }
)

