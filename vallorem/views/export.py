# -*- encoding: utf-8 -*-
# std python 
from __future__ import unicode_literals
from io import BytesIO as StringIO
import csv
from zipfile import ZipFile
# 3rd party lib import
from flask import flash, make_response

from vallorem import app
from vallorem.model import db, Production, Personne, ChgEquipe, DatePromotion
from vallorem.model import Doctorant, Equipe, TypeProduction
from vallorem.model import Mail, Observation, Statut, TypeFinancement
from vallorem.model.mail_personne import mail_personne
from vallorem.model.production_personne import production_personne

def clamp_to_utf8(obj):
    if not isinstance(obj, (str, unicode)):
        return obj
    return obj.encode('utf-8')

@app.route('/export/')
def export():
    objs = [Production, Personne, ChgEquipe, DatePromotion, Doctorant, Equipe,
        Mail, Observation, Statut, TypeFinancement, TypeProduction]
    relation_table = [mail_personne, production_personne]
    tables = [(x, [f.name for f in x.__table__.columns]) for x in objs]
    tables += [(x, [f.name for f in x.columns]) for x in relation_table]
    fichier = StringIO()
    zip = ZipFile(fichier, 'w')

    for obj, head in tables:
        output = StringIO()
        writer = csv.writer(output)
        with db.session() as s:
            lst = s.query(obj).all()
        writer.writerow(head)
        for element in lst:
            row = [getattr(element, attr) for attr in head]
            writer.writerow(map(clamp_to_utf8, row))
        zip.writestr(
            "export/%s.csv" % getattr(obj, '__name__', unicode(obj)),
            output.getvalue())

    zip.close()
    response = make_response(fichier.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=export.zip"
    return response
