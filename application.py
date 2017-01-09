__author__ = 'joyh'

from app.dbFunctions import *
from flask import Flask, render_template, request, redirect
from os.path import expanduser
from flask.ext.stormpath import StormpathManager, login_required, user, groups_required
from datetime import timedelta

app = Flask(__name__)

# app.config['SECRET_KEY'] = 'pij41li5j3reqw09u0t9p4ij23ehw8'
# # Not good practice!!! Need to fix the .properties file
# app.config['STORMPATH_API_KEY_ID'] = 'ZRKCGFJO05ZQT163UPAUA4CCX'
# app.config['STORMPATH_API_KEY_SECRET'] = 'Gn914B4EeItVJ+U/PgOaFVyXoq48IpTbM5m+I+gjsZQ'
# app.config['STORMPATH_APPLICATION'] = 'HootHousing'
#
# app.config['STORMPATH_COOKIE_DURATION'] = timedelta(minutes=60)
#
# # Storm Path Registration
# # app.config['STORMPATH_REGISTRATION_URL'] = '/registration'
# # app.config['STORMPATH_REGISTRATION_TEMPLATE'] = 'registration.html'
#
# # Storm Path Login
# app.config['STORMPATH_ENABLE_USERNAME'] = True
# app.config['STORMPATH_ENABLE_MIDDLE_NAME'] = False
# app.config['STORMPATH_ENABLE_USERNAME'] = True
# app.config['STORMPATH_ENABLE_FORGOT_PASSWORD'] = False
#
# stormpath_manager = StormpathManager(app)


app.config['SECRET_KEY'] = 'B5YLxYL33OBtvuF6GCxZk1B9vB7sfBZDGe6by7Y64Ds'
app.config['STORMPATH_API_KEY_FILE'] = expanduser('apiKey.properties')
app.config['STORMPATH_APPLICATION'] = 'HootHousing'

app.config['STORMPATH_COOKIE_DURATION'] = timedelta(minutes=60)

# Storm Path Login
app.config['STORMPATH_ENABLE_MIDDLE_NAME'] = False
app.config['STORMPATH_REQUIRE_MIDDLE_NAME'] = False
app.config['STORMPATH_ENABLE_USERNAME'] = True
app.config['STORMPATH_REQUIRE_USERNAME'] = True
app.config['STORMPATH_ENABLE_FORGOT_PASSWORD'] = True

stormpath_manager = StormpathManager(app)


# Get user from href
def href2user(href):
	username = None
	try:
		username = stormpath_manager.client.accounts.get(href).username
		pass
	except:
		return 'Unknown User'
	if username is None:
		return 'None'
	return username


# Enables use of global variables through Jinja
@app.context_processor
def inject_template_gloabls():
	return {
		'user': user,
	    'href2user': href2user
	}


# Inital Page
@app.route('/')
def index():
	flag = "false"
	return render_template('index.html', flag=flag)


# Redirect after login
@app.route('/loginBrowse')
@login_required
def loginBrowse():
	return redirect('/browse')


# Load Browse
@app.route('/browse')
def browse():
	results = getPropertiesDB(campus_id=1)
	return render_template('browse.html', results=results[0])


@app.route('/filterSubmission', methods=['POST'])
def filterSubmission():
	if request.method =='POST':
		distance    = request.form.get('distance')
		bedrooms    = request.form.get('bedrooms')
		bathrooms   = request.form.get('bathrooms')
		minRent     = request.form.get('min-rent')
		maxRent     = request.form.get('max-rent')
		unitType1   = request.form.get('unit-type-1')
		unitType2   = request.form.get('unit-type-2')
		unitType3   = request.form.get('unit-type-3')
		unitType4   = request.form.get('unit-type-4')

		unitType = []

		if unitType1 != None:
			unitType.append(unitType1)
		if unitType2 != None:
			unitType.append(unitType2)
		if unitType3 != None:
			unitType.append(unitType3)
		if unitType4 != None:
			unitType.append(unitType4)

		if distance == "null":
			if bedrooms =="null":
				if bathrooms == "null":
					if minRent == "null":
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1)
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								print results
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
					else:
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, min_rent=int(minRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, min_rent=int(minRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, min_rent=int(minRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, min_rent=int(minRent), max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, min_rent=int(minRent), max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
				else:
					if minRent == "null":
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
					else:
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), min_rent=int(minRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), min_rent=int(minRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), min_rent=int(minRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
			else:
				if bathrooms == "null":
					if minRent == "null":
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
					else:
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), min_rent=int(minRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), min_rent=int(minRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), min_rent=int(minRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), min_rent=int(minRent), max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
				else:
					if minRent == "null":
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
					else:
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
		else:
			if bedrooms =="null":
				if bathrooms == "null":
					if minRent == "null":
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance), max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
					else:
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance), min_rent=int(minRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), min_rent=int(minRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), min_rent=int(minRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance), min_rent=int(minRent), max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), min_rent=int(minRent), max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
				else:
					if minRent == "null":
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
					else:
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), min_rent=int(minRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), min_rent=int(minRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), min_rent=int(minRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
			else:
				if bathrooms == "null":
					if minRent == "null":
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
					else:
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), min_rent=int(minRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), min_rent=int(minRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), min_rent=int(minRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), min_rent=int(minRent), max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
				else:
					if minRent == "null":
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
					else:
						if maxRent == "null":
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])
						else:
							if len(unitType) == 0:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 1:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 2:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]))
								return render_template('browse.html', results=results[0])
							elif len(unitType) == 3:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]))
								return render_template('browse.html', results=results[0])
							else:
								results = getPropertiesDB(campus_id=1, distance=int(distance), beds=int(bedrooms), baths=int(bathrooms), min_rent=int(minRent), max_rent=int(maxRent), type_id=int(unitType[0]), type_id_2=int(unitType[1]), type_id_3=int(unitType[2]), type_id_4=int(unitType[3]))
								return render_template('browse.html', results=results[0])


@app.route('/mgmtReview/<manager_id>')
@login_required
def mgmtReview(manager_id):
	results = getManagementInfoDB(manager_id)
	return render_template('management-review.html', results=results[0][0], prop_results=results[1])


@app.route('/propReview/<property_id>')
@login_required
def propReview(property_id):
	results = getPropertyInfoDB(property_id)
	return render_template('review.html', results=results[0][0])


@app.route('/reviewSubmission', methods=['POST'])
@login_required
def reviewSubmission():
	if request.method == 'POST':
		title         = request.form.get('review_title')
		propRating    = request.form.get('property_rating')
		mgmtRating    = request.form.get('mgmt_rating')
		rent          = request.form.get('rent')
		review        = request.form.get('prop_review')
		recommend     = request.form.get('recommend')
		prop_id       = request.form.get('prop_id')


		if title == "" or rent =="" or review =="" or propRating == None or mgmtRating == None or recommend == None:
			return render_template('review.html')
		else:
			saveReviewDB(title=str(title.title()), text=str(review), manager_rating=int(mgmtRating), property_rating=int(propRating), recommended=int(recommend), property_id=prop_id, user_href=user.href, rent=int(rent))
			return render_template('submission.html')


@app.route('/addProperty')
@login_required
def addProperty():
	management,unitType,university = propertyFormInfoDB()
	return render_template('add-property.html', management=management, unitType=unitType, university=university)


@app.route('/propSubmission', methods=['POST'])
@login_required
def propSubmission():
	if request.method == 'POST':

		name         = request.form.get('prop_name')
		address      = request.form.get('street_address')
		num          = request.form.get('street_number')
		unit         = request.form.get('unit')
		city         = request.form.get('city')
		state        = request.form.get('state')
		zip          = request.form.get('zip')
		management   = request.form.get('management')
		bedrooms     = request.form.get('bedrooms')
		bathrooms    = request.form.get('bathrooms')
		unitType     = request.form.get('unit_type')
		university   = request.form.get('university')
		img          = None

		if name == "" or address =="" or city =="" or zip =="":
			return redirect('/addProperty')
		else:
			savePropertyDB(property_name=str(name.title()), street_number=str(num), street_name=str(address), unit=str(unit), city=str(city), state=str(state), zip=str(zip), manager_id=int(management), beds=int(bedrooms), baths=int(bathrooms), type_id=int(unitType), campus_id=university)
			return render_template('submission.html')


@app.route('/property/<property_id>')
def property(property_id):
	results = getPropertyInfoDB(property_id=property_id)
	return render_template('property.html', prop_results=results[0], review_results=results[1], href2user=href2user)


@app.route('/management/<management_id>')
def management(management_id):
	results = getManagementInfoDB(manager_id=management_id)
	return render_template('management.html', mgmt_results=results[0], prop_results=results[1])


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/contact')
def contact():
	return render_template('contact.html')


@app.route('/search', methods=['POST'])
def search():
	if request.method == 'POST':
		keyword = request.form.get('userSearch')
		alert = request.form.get('alert')
		flag = "false"
		print flag, alert
		if keyword == "" and alert == "true":
			flag = "true"
			print flag, alert
			return render_template('index.html', flag=flag)
		results = getPropertiesBySearchDB(campus_id=1, keyword=keyword)
	return render_template('browse.html', results=results[0], flag=flag)

@app.route('/terms')
def terms():
	return render_template('terms.html')

@app.route('/policy')
def policy():
	return render_template('policy.html')

@app.route('/FAQ')
def FAQ():
	return render_template('FAQ.html')

@app.route('/glossary')
def glossary():
	return render_template('glossary.html')

@app.route('/claim')
def claim():
	return render_template('claim.html')

@app.route('/subscribe')
def subscribe():
	return render_template('subscribe.html')

@app.route('/submission')
def submission():
	return render_template('submission.html')


if __name__ == '__main__':
	app.run(debug=True)