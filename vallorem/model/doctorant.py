from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from vallorem.model import Base, db
from vallorem.model.type_financement import TypeFinancement
from vallorem.model.observation import Observation


class Doctorant(Base):
    __tablename__ = 'doctorant'
    id = Column(Integer, primary_key=True)
    id_personne = Column(Integer, ForeignKey('personne.id'), nullable=False, unique=True)
    id_type_financement = Column(Integer, ForeignKey('type_financement.id'))
    id_observation = Column(Integer, ForeignKey('observation.id'))
    sujet_these = Column(String(500))
    nombre_ia = Column(Integer)
    date_soutenance = Column(DateTime)

    personne = relationship("Personne", lazy="immediate")
    _type_financement = relationship("TypeFinancement", lazy="joined")
    _observation = relationship("Observation", lazy="joined")

    def __str__(self):
        with db.session() as s:
            me = s.query(Doctorant).get(self.id)
            name = str(me.personne)
        return "Doctorant %s" % name

    @property
    def type_financement(self):
        if self._type_financement is None:
            return None
        return self._type_financement.description

    @type_financement.setter
    def type_financement(self, value):
        if isinstance(value, (str, unicode)):
            if self.type_financement == value:
                return
            value = TypeFinancement.get_or_create(value)
        self._type_financement = value

    @property
    def observation(self):
        if self._observation is None:
            return None
        return self._observation.description

    @type_financement.setter
    def observation(self, value):
        if isinstance(value, (str, unicode)):
            if value == self.observation:
                return
            value = Observation(value)
        self._observation = value
