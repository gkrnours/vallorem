from sqlalchemy import Column, Integer, String, ForeignKey

from vallorem.model import Base


class Page(Base):
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True)
    id_categorie = Column(Integer, ForeignKey('categorie.id'))
    titre = Column(String(255))
    content = Column(String(5000))


    def __init__(self, id_categorie,titre,content):
        self.id_categorie = id_categorie
        self.titre = titre
        self.content = content

    def __repr__(self):
        return "<Page(titre='%s')>" % self.titre

    def update_titre(self, new_titre):
        self.titre = new_titre