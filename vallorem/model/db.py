from flask import Flask
from sqlalchemy import distinct, func
from sqlalchemy.orm import scoped_session, sessionmaker
from flask.ext.sqlalchemy import SQLAlchemy
from vallorem import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/vallorem.db'
db = SQLAlchemy(app)

