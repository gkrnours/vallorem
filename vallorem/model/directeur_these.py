from db import db


class DirecteurThese(db.Model):
    id = db.Column(db.Integer, primary_key=True, sqlite_autoincrement=True)
    id_doctorant = db.Column(db.Integer, db.ForeignKey('personne.id'))
    id_directeur = db.Column(db.Integer, db.ForeignKey('personne.id'))

    def __init__(self, id_doctorant, id_directeur):
        self.id_doctorant = id_doctorant
        self.id_directeur = id_directeur
