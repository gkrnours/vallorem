# -*- encoding: utf-8 -*-
# std python 
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
import pelican

from vallorem import app
from vallorem.model import db, Page
from vallorem.utils import Capturing



@app.route('/build/')
def build():
    with Capturing() as output:
        pelican.main()
    if output[0].startswith("Done"):
        flash(output[0], category="success")
    if False:
	    for l in output:
    		flash(l)
    return redirect(url_for('dashboard'))
