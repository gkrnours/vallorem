# -*- encoding: utf-8 -*-
# std python 
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
from sqlalchemy import exc
# local import
from vallorem.form import PageForm
from vallorem.model import db, Page
from vallorem.views import utils
from vallorem import app

utils.make_crud(
    app, Page, PageForm,
    {'name':'page', 'path':'/page/', 'tpl':'site/page/'},
    msg = {
        "delete": 'La page «%s» a été supprimé.',
        "insert": {
            'success': "La page «%s» a été ajoutée.",
            'failure': "Les données saisies sont invalides",
        },
        "update": {
            "success": "La page «%s» a été modifiée.",
            "failure": "Les données saisies sont invalides",
        }
    }
)
