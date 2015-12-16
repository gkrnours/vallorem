from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from vallorem.model import Base
from vallorem.model.mail_personne import mail_personne
from vallorem.model.user_personne import user_personne
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

    info_doctorant = relationship("Doctorant")
    chgs_equipe = relationship("ChgEquipe", back_populates="personne")
    dates_promotion = relationship("DatePromotion", back_populates="personne")
    mails = relationship("Mail", secondary=mail_personne, back_populates="personnes")
    users = relationship("User", secondary=user_personne, back_populates="personnes")

    @property
    def statut(self):
        if self.statut is None:
            return None
        return self._statut.description

    @statut.setter
    def statut(self, value):
        self._statut = value
