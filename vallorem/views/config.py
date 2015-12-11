from flask import render_template
from flask import Flask, request, session, redirect, url_for, flash
from vallorem import app

@app.route('/config')
def config():
    onglet = {'sys': 'selected'}
    return redirect(url_for('page'))