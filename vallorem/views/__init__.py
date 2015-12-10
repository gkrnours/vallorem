# -*- encoding: utf-8 -*-
# std python import
from __future__ import unicode_literals

import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort
from flask import render_template, flash, redirect
from contextlib import closing
from vallorem.form import PageForm,CategorieForm,UserForm

from vallorem import app
from vallorem.views import login, page, categorie
from vallorem.views import user, config, index



@app.route('/site-map')
def site_map():
    """ Display the list of rules reachable with a browser and without
    parameters """
    links = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    return render_template('site_map.html', urls=links)
