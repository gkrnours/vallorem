from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from vallorem.model import Base
from vallorem.model.categorie import Categorie


class Page(Base):
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True)
    _categorie = relationship("Categorie", lazy="joined")
    categorie_id = Column(Integer, ForeignKey('categorie.id'))
    titre = Column(String(255))
    content = Column(String(5000))

    @property
    def categorie(self):
        if self._categorie is None:
            return None
        return self._categorie.description

    @categorie.setter
    def categorie(self, value):
        self._categorie = value
