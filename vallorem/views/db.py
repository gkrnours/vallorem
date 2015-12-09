# -*- encoding: utf-8 -*-
# std python import
from __future__ import unicode_literals

import os
from sqlite3 import dbapi2 as sqlite3
import click
from contextlib import closing

from vallorem import app


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    return rv


def init_db():
    """Initializes the database."""
    with closing(connect_db()) as db:
        with app.open_resource('vallorem.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@click.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def has_no_empty_params(rule):
    """return True if the rule can be used without arguments"""
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(arguments) <= len(defaults)
