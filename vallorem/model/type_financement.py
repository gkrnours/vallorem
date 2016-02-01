from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from vallorem.model import Base, db


class TypeFinancement(Base):
    __tablename__ = 'type_financement'
    id = Column(Integer, primary_key=True)
    description = Column(String(50))

    def __init__(self, description):
        self.description = description

    @classmethod
    def get_or_create(cls, name):
        with db.session() as s:
            tf = s.query(cls).filter(cls.description == name).one_or_none()
            if tf is None:
                tf = cls(name)
                s.add(tf)
        return tf
