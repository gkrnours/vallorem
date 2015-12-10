from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from vallorem.model import Base


class Doctorant(Base):
    __tablename__ = 'doctorant'
    id = Column(Integer, primary_key=True)
    id_personne = Column(Integer, ForeignKey('personne.id'))
    id_type_financement = Column(Integer, ForeignKey('type_financement.id'))
    id_observation = Column(Integer, ForeignKey('observation.id'))
    sujet_these = Column(String(500))
    nombre_ia = Column(Integer)
    date_soutenance = Column(DateTime)

    def __init__(self, id_personne, id_type_financement, id_observation,
                 sujet_these, nombre_ia, date_soutenance):

        self.id_personne = id_personne
        self.id_type_financement = id_type_financement
        self.id_observation = id_observation
        self.sujet_these = sujet_these
        self.nombre_ia = nombre_ia
        self.date_soutenance = date_soutenance
