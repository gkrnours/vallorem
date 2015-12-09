from db import db


class ProductionPersonne(db.Model):
    id = db.Column(db.Integer, primary_key=True, sqlite_autoincrement=True)
    id_production = db.Column(db.Integer, db.ForeignKey('production.id'))
    id_personne = db.Column(db.Integer, db.ForeignKey('personne.id'))

    def __init__(self, id_production, id_personne):
        self.id_production = id_production
        self.id_personne = id_personne
