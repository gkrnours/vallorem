from sqlalchemy import Column, Integer, String
from vallorem.model.db import Base


class Observation(Base):
    __tablename__ = 'observation'
    id = Column(Integer, primary_key=True)
    description = Column(String(500))

    def __init__(self, description):
        self.description = description
