from sqlalchemy import Table, Column, Integer, ForeignKey
from vallorem.model import Base

mail_personne = Table('mail_personne', Base.metadata,
                      Column('id_mail', Integer, ForeignKey('mail.id')),
                      Column('id_personne', Integer, ForeignKey('personne.id')))
