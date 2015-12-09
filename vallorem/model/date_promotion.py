from vallorem.model.db import db


class DatePromotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_personne = db.Column(db.Integer, db.ForeignKey('personne.id'))
    id_statut = db.Column(db.Integer, db.ForeignKey('statut.id'))
    date_promotion = db.Column(db.DateTime)

    def __init__(self, id_personne, id_statut, date_promotion):
        self.id_personne = id_personne
        self.id_statut = id_statut
        self.date_promotion = date_promotion
