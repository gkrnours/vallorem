from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from vallorem import app
from vallorem.model import Base
from vallorem.model import categorie, page
from vallorem.model import personne, user, user_personne, statut, date_promotion
from vallorem.model import directeur_these, doctorant, type_financement
from vallorem.model import mail, mail_personne
from vallorem.model import equipe, chg_equipe
from vallorem.model import production, production_personne, type_production, observation

engine = create_engine('sqlite:///db/vallorem.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base.query = db_session.query_property()


def init_db():
    """import all modules here that might define models so that
    they will be registered properly on the metadata.  Otherwise
    you will have to import them first before calling init_db()"""

    Base.metadata.create_all(bind=engine)


@contextmanager
def session():
    session = db_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()