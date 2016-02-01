# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import request, session, redirect, url_for, flash
from flask import render_template
from sqlalchemy import exc
# local import
from vallorem import app
from vallorem.form import TypeProductionForm
from vallorem.model import db, TypeProduction
from vallorem.views import utils

def insert(form):
    typeProd = TypeProduction(form.description.data, form.publication.data)
    try:
        with db.session() as s:
            s.add(typeProd)
        flash('Le type de production «%s» a été ajouté.' % typeProd)
        return True
    except exc.IntegrityError:
        flash('Les données saisies sont invalide.')
        return False

utils.make_crud(
    app, TypeProduction, TypeProductionForm,
    {'name':'prod.type','path':'/typeproduction/','tpl':'production/type/'},
    insert,
    msg = {
        'delete': 'Le type de production «%s» a été supprimé.',
        'update': {
            'success': 'Le type de production «%s» a été modifié.',
            'failure': 'Les données saisies sont invalide.',
        }
    }
)
