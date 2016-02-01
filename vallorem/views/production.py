# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem import app
from vallorem.model import db, Production
from vallorem.form import ProductionForm
from vallorem.views import utils

utils.make_crud(
    app, Production, ProductionForm,
    {'name':'production', 'path':'/production/', 'tpl':'production/'},
    msg = {
        'delete': 'La production %s a été supprimée.',
        'insert': {
            'success': "La production «%s» a été ajoutée.",
            'failure': "Les données saisies sont invalide.",
        },
        'update': {
            'success': "La production «%s» a été modifiée.",
            'failure': "Les données saisies sont invalide.",
        }
    }
)
