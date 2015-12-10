from sqlalchemy import Column, Integer, ForeignKey
from vallorem.model.db import Base


class MailPersonne(Base):
    __tablename__ = 'mail_personne'
    id = Column(Integer, primary_key=True)
    id_personne = Column(Integer, ForeignKey('personne.id'))
    id_mail = Column(Integer, ForeignKey('mail.id'))

    def __init__(self, id_personne, id_mail):
        self.id_personne = id_personne
        self.id_mail = id_mail
