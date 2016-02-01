from sqlalchemy import Column, Integer, String, Boolean
from vallorem.model import Base


class TypeProduction(Base):
    __tablename__ = 'type_production'
    id = Column(Integer, primary_key=True)
    description = Column(String(500))
    publication = Column(Boolean)

    def __init__(self, description, publication=True):
        self.description = description
        self.publication = publication

    def __str__(self):
        return self.description
