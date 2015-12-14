from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from vallorem.model import Base


class Statut(Base):
    __tablename__ = 'statut'
    id = Column(Integer, primary_key=True)
    description = Column(String(50))

    personnes = relationship("Personne")
    dates_promotion = relationship("DatePromotion")

    def __init__(self, description):
        self.description = description
