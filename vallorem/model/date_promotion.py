from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from vallorem.model import Base, db, Statut


class DatePromotion(Base):
    __tablename__ = 'date_promotion'
    id = Column(Integer, primary_key=True)
    id_personne = Column(Integer, ForeignKey('personne.id'))
    id_statut = Column(Integer, ForeignKey('statut.id'))
    date_promotion = Column(Date)

    _statut = relationship("Statut", lazy="joined")
    personne = relationship("Personne", lazy="joined",
        back_populates="dates_promotion")

    def __str__(self):
        with db.session() as s:
            me = s.query(DatePromotion).get(self.id)
            name = str(me.personne)
        return "%s devient %s" % (name, self.statut)

    @property
    def statut(self):
        if self._statut is None:
            return None
        return self._statut.description

    @statut.setter
    def statut(self, value):
        if isinstance(value, (str, unicode)):
            if self.statut == value:
                return
            value = Statut.get_or_create(value)
        self._statut = value
