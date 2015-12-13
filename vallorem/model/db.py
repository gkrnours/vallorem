from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from vallorem import app
from vallorem.model import Base

db_session = None
_engine = None


def create(engine=None):
    """import all modules here that might define models so that
    they will be registered properly on the metadata.  Otherwise
    you will have to import them first before calling init_db()"""
    from vallorem.model import Categorie, Page, Mail
    if engine is None:
        if _engine is None:
            engine = init()
        else:
            engine = _engine
    Base.metadata.create_all(bind=engine)

"""
def clean(engine=None):
    if engine is None:
        if _engine is None:
            engine = init()
        else:
            engine = _engine
        engine = init()
    Base.metadata.drop_all(
"""


def init(engine=None, autoflush=False):
    global db_session
    global _engine
    if engine is None:
        engine = create_engine(app.config['DATABASE'], convert_unicode=True)
    _engine = engine
    if db_session == None:
        options = {
            'autocommit': False,
            'autoflush': autoflush,
            'expire_on_commit': False,
            'bind': engine,
        }
        db_session = scoped_session(sessionmaker(**options))
    return engine


def get_engine():
    return _engine

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
