from sqlalchemy import Column, Integer, DateTime, ForeignKey
from vallorem.model import Base


class ChgEquipe(Base):
    __tablename__ = 'chg_equipe'
    id = Column(Integer, primary_key=True)
    id_personne = Column(Integer, ForeignKey('personne.id'))
    id_equipe = Column(Integer, ForeignKey('equipe.id'))
    date_chg = Column(DateTime)

    def __init__(self, id_personne, id_equipe, date_chg):
        self.id_personne = id_personne
        self.id_equipe = id_equipe
        self.date_chg = date_chg
