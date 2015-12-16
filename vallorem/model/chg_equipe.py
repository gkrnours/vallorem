from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from vallorem.model import Base
from vallorem.model.equipe import Equipe


class ChgEquipe(Base):
    __tablename__ = 'chg_equipe'
    id = Column(Integer, primary_key=True)
    id_personne = Column(Integer, ForeignKey('personne.id'))
    id_equipe = Column(Integer, ForeignKey('equipe.id'))
    date_chg = Column(DateTime)


    personne = relationship("Personne", back_populates="chgs_equipe")
    equipe = relationship("Equipe")

