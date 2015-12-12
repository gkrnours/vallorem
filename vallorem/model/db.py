from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from vallorem import app
from vallorem.model import Base

db_session = None


def create():
    """import all modules here that might define models so that
    they will be registered properly on the metadata.  Otherwise
    you will have to import them first before calling init_db()"""
    from vallorem.model import Categorie, Page
    engine = init()
    Base.metadata.create_all(bind=engine)


def init(engine=None):
    global db_session
    if engine is None:
        engine = create_engine(app.config['DATABASE'], convert_unicode=True)
    options = {
        'autocommit': False,
        'autoflush': False,
        'expire_on_commit': False,
        'bind': engine,
    }
    db_session = scoped_session(sessionmaker(**options))
    return engine


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
