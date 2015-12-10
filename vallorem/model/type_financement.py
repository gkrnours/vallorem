from sqlalchemy import Column, Integer, String
from vallorem.model.db import Base


class TypeFinancement(Base):
    __tablename__ = 'type_financement'
    id = Column(Integer, primary_key=True)
    description = Column(String(50))

    def __init__(self, description):
        self.description = description
