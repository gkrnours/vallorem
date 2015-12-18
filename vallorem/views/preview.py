# -*- encoding: utf-8 -*-
# std python 
from __future__ import unicode_literals
# 3rd party lib import
#from flask import Flask, request, session, redirect, url_for, flash

from vallorem import app
from vallorem.utils import templated



@app.route('/preview/')
@templated()
def preview():
    pass
