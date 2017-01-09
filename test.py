__author__ = 'gregoryhenkhaus'

from app.dbFunctions import *

list = getPropertiesDB(campus_id=None, distance=None, beds=None, baths=None, min_rent=None, max_rent=None, type_id=None, manager_id=None, property_id=None, type_id_2=1, type_id_3=3, type_id_4=4)


for thing in list:
	print '#' * 50
	for line in thing:
		print line
