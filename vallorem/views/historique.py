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
from vallorem.views import utils

utils.make_crud(
    app, DatePromotion, DatePromotionForm,
    {'name':'promotion', 'path':'/promotion/', 'tpl':'historique/promo/'},
    msg = utils.messages('La promotion', feminin=True)
)
