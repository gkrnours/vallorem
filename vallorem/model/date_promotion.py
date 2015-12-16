from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from vallorem.model import Base


class DatePromotion(Base):
    __tablename__ = 'date_promotion'
    id = Column(Integer, primary_key=True)
    id_personne = Column(Integer, ForeignKey('personne.id'))
    id_statut = Column(Integer, ForeignKey('statut.id'))
    date_promotion = Column(DateTime)

    _statut = relationship("Statut", lazy="joined")
    personne = relationship("Personne", back_populates="dates_promotion")

    @property
    def statut(self):
        return self._statut.description

    @statut.setter
    def statut(self, value):
        self._statut = value
