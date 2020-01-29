#!/usr/bin/env python3
# -*- coding: euc-kr -*-

import sys
import pyodbc

connect_string = "DSN=foms;UID=jilee;PWD=snrnrp47"
_CONN = None

def init_db_conn(connect_string):
	"""initializes db connections"""
	global _CONN
	if not _CONN:
		dbinfo = connect_string

		try:
			_CONN = pyodbc.connect(connect_string)
		except:
			ex = sys.exc_info()
			s = 'Exception: %s: %s\n%s' % (ex[0], ex[1], dbinfo)
			print(s)
			return None
	return _CONN

def main():
    """main"""
    if not init_db_conn(connect_string):
        print('Something is terribly wrong with db connection')
    else:
        print('DB Connection Success')

if __name__ == '__main__':
    main()