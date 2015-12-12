from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from vallorem.model import Base


class Observation(Base):
    __tablename__ = 'observation'
    id = Column(Integer, primary_key=True)
    description = Column(String(500))

    doctorants = relationship("Doctorant")

    def __init__(self, description):
        self.description = description
