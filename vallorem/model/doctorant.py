from vallorem.model.db import db


class Doctorant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_personne = db.Column(db.Integer, db.ForeignKey('personne.id'))
    id_type_financement = db.Column(db.Integer, db.ForeignKey('type_financement.id'))
    id_observation = db.Column(db.Integer, db.ForeignKey('observation.id'))
    sujet_these = db.Column(db.String(500))
    nombre_ia = db.Column(db.Integer)
    date_soutenance = db.Column(db.DateTime)

    def __init__(self, id_personne, id_type_financement, id_observation,
                 sujet_these, nombre_ia, date_soutenance):

        self.id_personne = id_personne
        self.id_type_financement = id_type_financement
        self.id_observation = id_observation
        self.sujet_these = sujet_these
        self.nombre_ia = nombre_ia
        self.date_soutenance = date_soutenance
