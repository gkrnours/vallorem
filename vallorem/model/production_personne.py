from sqlalchemy import Column, Integer, ForeignKey
from vallorem.model.db import Base


class ProductionPersonne(Base):
    __tablename__ = 'production_personne'
    id = Column(Integer, primary_key=True)
    id_production = Column(Integer, ForeignKey('production.id'))
    id_personne = Column(Integer, ForeignKey('personne.id'))

    def __init__(self, id_production, id_personne):
        self.id_production = id_production
        self.id_personne = id_personne
