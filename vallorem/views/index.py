# -*- coding: utf-8 -*-

# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
# local import

from vallorem import app

@app.route('/')
def home():
    return redirect('index')

@app.route('/index')
def index():
    return redirect('dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')