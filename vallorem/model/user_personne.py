from sqlalchemy import Column, Integer, ForeignKey
from vallorem.model import Base


class UserPersonne(Base):
    __tablename__ = "user_personne"
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_personne = Column(Integer, ForeignKey('personne.id'))

    def __init__(self, id_user, id_personne):
        self.is_user = id_user
        self.id_personne = id_personne
