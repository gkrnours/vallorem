from sqlalchemy import Column, Integer, String, ForeignKey
from vallorem.model import Base
from flask.ext.login import UserMixin



class User(Base,UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    id_mail = Column(Integer, ForeignKey('mail.id'))
    password = Column(String(50))

    def __init__(self, id_mail, password):
        self.id_mail = id_mail
        self.password = password

		
