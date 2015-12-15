from sqlalchemy import Table, Column, Integer, ForeignKey
from vallorem.model import Base

production_personne = Table('production_personne', Base.metadata,
                      Column('id_production', Integer, ForeignKey('production.id')),
                      Column('id_personne', Integer, ForeignKey('personne.id')))
