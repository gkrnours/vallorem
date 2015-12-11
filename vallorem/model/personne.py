from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from vallorem.model import Base


class Personne(Base):
    __tablename__ = 'personne'
    id = Column(Integer, primary_key=True)
    id_statut = Column(Integer, ForeignKey('statut.id'))
    id_equipe = Column(Integer, ForeignKey('equipe.id'))
    nom = Column(String(50))
    nom_jf = Column(String(50))
    prenom = Column(String(50))
    date_naissance = Column(DateTime)
    date_recrutement = Column(DateTime)
    permanent = Column(Boolean)


    def __init__(self, id_statut, id_equipe, nom, nom_jf, prenom,
                 date_naissance, date_recrutement, permanent):
        self.id_statut = id_statut
        self.id_equipe = id_equipe
        self.nom = nom
        self.nom_jf = nom_jf
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.date_recrutement = date_recrutement
        self.permanent = permanent
