from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from vallorem.model import Base
from vallorem.model.type_financement import TypeFinancement
from vallorem.model.observation import Observation


class Doctorant(Base):
    __tablename__ = 'doctorant'
    id = Column(Integer, primary_key=True)
    id_personne = Column(Integer, ForeignKey('personne.id'))
    id_type_financement = Column(Integer, ForeignKey('type_financement.id'))
    id_observation = Column(Integer, ForeignKey('observation.id'))
    sujet_these = Column(String(500))
    nombre_ia = Column(Integer)
    date_soutenance = Column(DateTime)

    personne = relationship("Personne", back_populates="doctorant")
    _type_financement = relationship("TypeFinancement", lazy="joined")
    _observation = relationship("Observation", lazy="joined")

    @property
    def type_financement(self):
        return self._type_financement.description

    @type_financement.setter
    def type_financement(self, value):
        self._type_financement = value

    @property
    def observation(self):
        return self._observation.description

    @type_financement.setter
    def observation(self, value):
        self._observation = value