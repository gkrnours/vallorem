# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from flask import request, flash, url_for
from flask import render_template, redirect
from sqlalchemy import exc

from vallorem.model import db

def messages(subject, feminin=False):
    suffix = 'e' if feminin else ''
    return {
        'delete': "%s «%s» a été supprimé%s" % (subject, '%s', suffix),
        'insert': {
            'success': "%s «%s» a été ajouté%s" % (subject, '%s', suffix),
            'failure': "Les données saisies sont invalide"
        },
        'update': {
            'success': "%s «%s» a été modifié%s" % (subject, '%s', suffix),
            'failure': "Les données saisies sont invalide",
        },
    }

def generic_insert(model, msg):
    def aux(form):
        obj = model()
        form.populate_obj(obj)
        try:
            with db.session() as s:
                s.add(obj)
            flash(msg['success'] % obj, category="success")
            return True
        except exc.IntegrityError:
            flash(msg['failure'], category="danger")
            return False
    return aux

def generic_update(msg):
    def aux(form, obj):
        form.populate_obj(obj)
        try:
            with db.session() as s:
                s.add(obj)
            flash(msg['success'] % obj)
            return True
        except exc.IntegrityError:
            flash(msg['failure'], category="danger")
            return False
    return aux

# --

def read(model, tpl):
    def aux():
        ctx = {}
        with db.session() as s:
            ctx['list'] = s.query(model).all()
        return render_template(tpl, **ctx)
    return aux

def create(formClass, insert, next, tpl):
    def aux():
        ctx = {}
        ctx['form'] = form = formClass(request.form)

        if request.method == "POST" and form.validate() and insert(form):
            return redirect(url_for(next))

        return render_template(tpl, **ctx)
    return aux

def update(model, formClass, update, next, tpl):
    def aux(id):
        ctx = {}
        with db.session() as s:
            obj = s.query(model).get(id)
        ctx['form'] = form = formClass(request.form, obj)

        if request.method == "POST" and form.validate() and update(form, obj):
            return redirect(url_for(next))

        return render_template(tpl, **ctx)
    return aux

def delete(model, next, msg=""):
    def aux(id, name="unknown"):
        with db.session() as s:
            count = s.query(model).filter(model.id == id).delete()
        if count and msg:
            flash(msg % name, category="danger")
        return redirect(url_for(next))
    return aux

def make_crud(app, model, form, prefix, _insert=None, _update=None, msg=None):
    """app: the flask app
       model: the model to use
       form: the form class to use
       prefix: dict with name, path and tpl prefix
       insert: take a form and return true if an object have been inserted
       update: take a form and an item, return true if an object is update
    """
    if _insert is None:
        _insert = generic_insert(model, msg['insert'])
    if _update is None:
        _update = generic_update(msg['update'])

    # list
    app.add_url_rule("%s" % prefix['path'], "%s" % prefix['name'],
        read(model, "%slist.html" % prefix['tpl'])
    )
    # create
    app.add_url_rule("%sajout" % prefix['path'], "%s.create" % prefix['name'],
        create(form, _insert, prefix['name'], "%sajout.html" % prefix['tpl']),
        methods=['GET', 'POST'],
    )
    # update
    app.add_url_rule(
        "%smodif/<int:id>" % prefix['path'],
        "%s.update" % prefix['name'],
        update(model, form, _update, prefix['name'],
            "%sajout.html" % prefix['tpl']),
        methods=['GET', 'POST'],
    )
    # delete
    app.add_url_rule(
        "%sdelete/<int:id>_<name>" % prefix['path'],
        "%s.delete" % prefix['name'],
        delete(model, prefix['name'], msg['delete'])
    )
