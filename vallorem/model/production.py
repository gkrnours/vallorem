from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from vallorem.model.db import Base


class Production(Base):
    __tablename__ = 'production'
    id = Column(Integer, primary_key=True)
    id_type = Column(Integer, ForeignKey('type_production.id'))
    titre = Column(String(50))
    description = Column(String(5000))
    extra = Column(String(5000))
    date = Column(DateTime)

    def __init__(self, id_type, titre, description, extra, date):
        self.id_type = id_type
        self.titre = titre
        self.description = description
        self.extra = extra
        self.date = date
