#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

import argparse

from vallorem import start
from vallorem.model import db

parser = argparse.ArgumentParser(description="Vallorem")
parser.add_argument("--initdb", dest='initdb', action="store_true")
args = parser.parse_args()

if args.initdb:
    db.create()
    print('La base de données a été initialisée')
else:
    start(debug=True)
