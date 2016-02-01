# -*- coding: utf-8 -*-
# std python import
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem import app
from vallorem.form import DoctorantForm, PersonneForm
from vallorem.model import db, Categorie, Personne, Doctorant, Statut
from vallorem.model import Observation, TypeFinancement
from vallorem.views import utils


utils.make_crud(
    app, Doctorant, DoctorantForm,
    {"name": 'doctorant', 'path':'/doctorant/', 'tpl': 'doctorant/'},
    msg = utils.messages('Le doctorant')
)

