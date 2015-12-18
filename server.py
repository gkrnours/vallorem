#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

import argparse
from subprocess import Popen

import vallorem

parser = argparse.ArgumentParser(description="Vallorem")
parser.add_argument("--initdb", dest='initdb', action="store_true")
args = parser.parse_args()

if args.initdb:
    vallorem.model.db.create()
    print('La base de données a été initialisée')
else:
    server = Popen(['darkhttpd', 'output', '--port', '2500'])
    vallorem.start(debug=True)
    server.terminate()
