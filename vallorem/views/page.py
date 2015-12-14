# -*- encoding: utf-8 -*-
# std python 
from __future__ import unicode_literals
# 3rd party lib import
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
# local import
from vallorem.form import PageForm
from vallorem.model import db, Page
from vallorem import app

@app.route('/page/')
def page(action=None):
    ctx = {}
    with db.session() as s:
        ctx['pages'] = s.query(Page).all()
    ctx['page'] = {'sys': 'selected'}
    ctx['form'] = PageForm()
    return render_template('page/page.html', **ctx)

@app.route('/page/ajout', methods=['GET', 'POST'])
def pageAjout():
    onglet = {'sys': 'selected'}
    form = PageForm(request.form)
    if request.method == "POST" and form.validate():
        p = Page(titre=form.title.data, categorie_id=form.categorie.data,
            content=form.contenu.data)
        with db.session() as s:
            s.add(p)
        flash('Vous avez ajouté la page %s.'%form.title.data, 'success')
        return redirect('page')
    elif form.errors:
        flash('\n'.join(form.errors), 'error')
    return render_template('page/ajout.html', page=onglet, form=form)

@app.route('/page/modif', methods=['GET', 'POST'])
def pageModif():
    form=PageForm()
    onglet = {'sys': 'selected'}
    if request.method == "POST":
    #ecrire des codes pour ajouter input dans la base de donnees
        form = PageForm(request.form)
    return render_template('page/ajout.html', page=onglet, form=form)

@app.route('/page/delete')
@app.route('/page/delete/<id>')
def pageDelete(id):

    with db.session() as s:
        s.query(Page).filter(Page.id == id).delete()
    return redirect(url_for('page'))
