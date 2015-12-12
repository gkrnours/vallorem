from sqlalchemy import Table, Column, Integer, ForeignKey
from vallorem.model import Base

user_personne = Table('user_personne', Base.metadata,
                      Column('id_user', Integer, ForeignKey('user.id')),
                      Column('id_personne', Integer, ForeignKey('personne.id')))
