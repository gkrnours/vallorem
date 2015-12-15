from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from vallorem.model.personne import Personne
from vallorem.model.doctorant import Doctorant
from vallorem.model import Base


class DirecteurThese(Base):
    __tablename__ = 'directeur_these'
    id = Column(Integer, primary_key=True)
    id_doctorant = Column(Integer, ForeignKey('personne.id'))
    id_directeur = Column(Integer, ForeignKey('personne.id'))


    directeur = relationship("Personne", lazy="joined")
    doctorant = relationship("Personne", lazy="joined")
    info_doctorant = relationship("Doctorant", lazy="joined")