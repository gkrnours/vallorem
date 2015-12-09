from vallorem.model.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_personne = db.Column(db.Integer, db.ForeignKey('personne.id'))
    id_equipe = db.Column(db.Integer, db.ForeignKey('equipe.id'))
    date_chg = db.Column(db.DateTime)

    def __init__(self, id_personne, id_equipe, date_chg):
        self.id_personne = id_personne
        self.id_equipe = id_equipe
        self.date_chg = date_chg
