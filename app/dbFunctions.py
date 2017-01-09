__author__ = 'joyh'

from app.db import *

# General
def getPropertiesDB(campus_id=None, distance=None, beds=None, baths=None, min_rent=None, max_rent=None, type_id=None, manager_id=None, property_id=None, type_id_2=None, type_id_3=None, type_id_4=None):
	try:
		if type_id is None and type_id_2 is None and type_id_3 is None and type_id_4 is None:
			results = storedProcedureList(procedure='get_properties', parameter=(campus_id, distance, beds, baths, min_rent, max_rent, type_id, manager_id, property_id, type_id_2, type_id_3, type_id_4))
		else:
			results = storedProcedureList(procedure='get_properties_filter', parameter=(campus_id, distance, beds, baths, min_rent, max_rent, type_id, manager_id, property_id, type_id_2, type_id_3, type_id_4))
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		return None
	return results


# Browse Page
def getPropertiesBySearchDB(campus_id=None, keyword=''):
	try:
		results = storedProcedureList('get_properties_by_search', parameter=(campus_id, keyword))
	except:
		return None
	return results


# Add Review Page
def saveReviewDB(title=None, text=None, manager_rating=None, property_rating=None, recommended=None, property_id=None, user_href=None, rent=None):
	try:
		results = storedProcedureList(procedure='save_review', parameter=(title, text, manager_rating, property_rating, recommended, property_id, user_href, rent))
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		return None
	return results


# Add Property Page
def savePropertyDB(property_name='', street_number='', street_name='', unit='', city='', state='', zip='', manager_id=None, img_href=None, beds=0, baths=0, type_id=None, distance=0, campus_id=0):
	try:
		results = storedProcedureList(procedure='add_property', parameter=(property_name, street_number,street_name, unit, city, state, zip, manager_id, img_href, beds, baths, type_id, distance, campus_id))
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		return None
	return results


# Property Form Info
def propertyFormInfoDB():
	try:
		results = storedProcedureList(procedure='get_prop_form_info', parameter=())
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		return None
	return results


# Property Page
def getPropertyInfoDB(property_id=None):
	try:
		results = storedProcedureList(procedure='get_property_info', parameter=(property_id,))
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		return None
	return results

# Management Page
def getManagementInfoDB(manager_id=None):
	try:
		results = storedProcedureList(procedure='get_management_info', parameter=(manager_id,))
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		return None
	return results