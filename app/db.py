__author__ = 'joyh'

from app import config
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

configDB = {	'user': config.DBuser,
				'password': config.DBpassword,
				'host': config.DBhost,
				'port': config.DBport,
				'database': config.DBdatabase,
				'raise_on_warnings': config.DBraise_on_warnings,
				'autocommit': config.DBautocommit,
                'pool_name': config.DBpool_name,
                'pool_size': config.DBpool_size
				}

def query(query='', parameters=()):
	cnx = mysql.connector.connect(**configDB)
	if cnx.is_connected():
		# print('database connection established.')
		pass
	else:
		print('database connection failed.')
	cursor = cnx.cursor()
	cursor.execute(query, parameters)
	result = cursor.fetchall()
	cnx.close()
	return result

# Returns Args
def storedProcedureArgs(procedure='', parameter=()):
	cnx = mysql.connector.connect(**configDB)
	if cnx.is_connected():
		# print('database connection established.')
		pass
	else:
		print('database connection failed.')
	cursor = cnx.cursor()
	result_args = cursor.callproc(procedure, parameter)
	cnx.close()
	return result_args

# Returns List
def storedProcedureList(procedure='', parameter=()):
	resultList = []
	cnx = mysql.connector.connect(**configDB)
	if cnx.is_connected():
		# print('database connection established.')
		pass
	else:
		print('database connection failed.')
	cursor = cnx.cursor()
	cursor.callproc(procedure, parameter)

	for result in cursor.stored_results():
		resultList.append(result.fetchall())

	cnx.close()
	return resultList