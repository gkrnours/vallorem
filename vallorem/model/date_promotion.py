from sqlalchemy import Column, Integer, ForeignKey, DateTime
from vallorem.model.db import Base


class DatePromotion(Base):
    __tablename__ = 'date_promotion'
    id = Column(Integer, primary_key=True)
    id_personne = Column(Integer, ForeignKey('personne.id'))
    id_statut = Column(Integer, ForeignKey('statut.id'))
    date_promotion = Column(DateTime)

    def __init__(self, id_personne, id_statut, date_promotion):
        self.id_personne = id_personne
        self.id_statut = id_statut
        self.date_promotion = date_promotion
