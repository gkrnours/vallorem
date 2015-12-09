from flask import render_template
from vallorem import app

@app.route('/config')
def config():
    onglet = {'sys': 'selected'}
    return render_template('page/page.html', page=onglet)