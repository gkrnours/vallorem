from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from vallorem.model import Base, db


class Statut(Base):
    __tablename__ = 'statut'
    id = Column(Integer, primary_key=True)
    description = Column(String(50))

    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description

    @classmethod
    def get_or_create(cls, statut):
        with db.session() as s:
            st = s.query(cls).filter(Statut.description == statut).first()
            if st is None:
                st = cls(statut)
                s.add(st)
        return st
