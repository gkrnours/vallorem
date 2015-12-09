from db import db


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True, sqlite_autoincrement=True)
    id_categorie = db.Column(db.Integer, db.ForeignKey('categorie.id'))
    titre = db.Column(db.String(255))
    content = db.Column(db.String())