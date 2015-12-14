from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from vallorem.model import Base


class Production(Base):
    __tablename__ = 'production'
    id = Column(Integer, primary_key=True)
    id_type = Column(Integer, ForeignKey('type_production.id'), nullable=False)
    titre = Column(String(50))
    description = Column(String(5000))
    extra = Column(String(5000))
    date = Column(DateTime)

    type = relationship("TypeProduction", lazy="joined")

