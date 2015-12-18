from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from vallorem.model import Base
from vallorem.model.type_production import TypeProduction
from vallorem.model.production_personne import production_personne


class Production(Base):
    __tablename__ = 'production'
    id = Column(Integer, primary_key=True)
    id_type = Column(Integer, ForeignKey('type_production.id'))
    titre = Column(String(50))
    description = Column(String(5000))
    extra = Column(String(5000))
    date = Column(DateTime)

    type = relationship("TypeProduction", lazy="joined")
    personnes = relationship("Personne", secondary=production_personne, back_populates="productions")

