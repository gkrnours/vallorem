from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from vallorem.model import Base


class Categorie(Base):
    __tablename__ = 'categorie'
    id = Column(Integer, primary_key=True)
    description = Column(String(50))

    pages = relationship("page", order_by="page.id", backref="categorie")

    def __init__(self, description):
        self.description = description
