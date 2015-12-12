from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from vallorem.model import Base


class Equipe(Base):
    __tablename__ = 'equipe'
    id = Column(Integer, primary_key=True)
    nom = Column(String(50))
    axe = Column(String(50))
    localisation = Column(String(40))

    personnes = relationship("Personne")

    def __init__(self, nom, axe, localisation):
        self.nom = nom
        self.axe = axe
        self.localisation = localisation
