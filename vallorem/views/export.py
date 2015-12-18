# -*- encoding: utf-8 -*-
# std python 
from __future__ import unicode_literals
from io import BytesIO as StringIO
import csv
from zipfile import ZipFile
# 3rd party lib import
from flask import flash, make_response

from vallorem import app
from vallorem.model import db, User, Production, Personne


@app.route('/export/')
def export():
    objs = [User, Production, Personne]
    tables = [(x, [f.name for f in x.__table__.columns]) for x in objs]
    fichier = StringIO()
    zip = ZipFile(fichier, 'w')

    for obj, head in tables:
        output = StringIO()
        writer = csv.writer(output)
        with db.session() as s:
            lst = s.query(obj).all()
        writer.writerow(head)
        for element in lst:
            writer.writerow([getattr(element, at) for at in head])
        zip.writestr("%s.csv" % obj.__name__, output.getvalue())

    zip.close()
    response = make_response(fichier.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=export.zip"
    return response
