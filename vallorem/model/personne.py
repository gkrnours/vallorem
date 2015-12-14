from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from vallorem.model import Base
from vallorem.model.statut import Statut
from vallorem.model.equipe import Equipe

class Personne(Base):
    __tablename__ = 'personne'
    id = Column(Integer, primary_key=True)
    statut_id = Column(Integer, ForeignKey('statut.id'))
    _statut = relationship("Statut", lazy="joined")
    equipe_id = Column(Integer, ForeignKey('equipe.id'))
    equipe = relationship("Equipe", lazy="joined")
    nom = Column(String(50))
    nom_jf = Column(String(50))
    prenom = Column(String(50))
    date_naissance = Column(DateTime)
    date_recrutement = Column(DateTime)
    permanent = Column(Boolean)

    #dates_promotion = relationship("DatePromotion")
    #mails = relationship("Mail", secondary=mail_personne)


    @property
    def statut(self):
        return self._statut.description

    @statut.setter
    def statut(self, value):
        self._statut = value
