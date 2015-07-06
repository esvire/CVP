#!/usr/bin/python
# -*- coding: utf-8 -*-

import _mysql
import sys

try:
    coneccion = _mysql.connect('localhost', 'root', '12345', 'db_club')

    coneccion.query("SELECT VERSION()")
    result = coneccion.use_result()

    print "MySQL version: %s" % \
        result.fetch_row()[0]

except _mysql.Error, e:

    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:

    if coneccion:
        coneccion.close()

