from sqlalchemy import Column, Integer, ForeignKey
from vallorem.model import Base


class DirecteurThese(Base):
    __basename__ = 'directeur_these'
    id = Column(Integer, primary_key=True)
    id_doctorant = Column(Integer, ForeignKey('personne.id'))
    id_directeur = Column(Integer, ForeignKey('personne.id'))

    def __init__(self, id_doctorant, id_directeur):
        self.id_doctorant = id_doctorant
        self.id_directeur = id_directeur
