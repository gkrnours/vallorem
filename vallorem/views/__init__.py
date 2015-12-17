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
from vallorem.views import user, config, index, production, typeProduction
from vallorem.views import doctorant, typeFinancement, personne, datePromotion



@app.template_filter('wc')
def compteMot(string):
	l = string.split()
	return len(l)


