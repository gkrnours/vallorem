#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

import argparse
from vallorem import app

from vallorem.model.db import init_db


parser = argparse.ArgumentParser(description="Vallorem")
parser.add_argument("--initdb", dest='initdb', action="store_true")
args = parser.parse_args()

if args.initdb:
    init_db()
    print 'La base de données a été initialisée'
else:
    app.run(debug=True)