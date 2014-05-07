import urllib2
import json
import cPickle as pickle
import os, sys, time

# I chose not to validate a zip code. I did test and the API I'm using only accepts 5 digit US zip codes.
zipcode = raw_input('Enter a zip code to view current weather: ')

API_URL = 'http://api.worldweatheronline.com/free/v1/weather.ashx?q=%s&format=json&fx=no&key=uy99bzrx9w2xt575bymbjz97' % zipcode


# 2Do
# - Remove API key before submitting

def loadData():
	'''
	Makes the API call to the URL and returns the json data as a python object.
	API call returns json data. This data is converted to python object.

	Returns: python object.
	'''
	return json.loads(urllib2.urlopen(API_URL).read())

def cacheData(filename, data):
	'''
	Writes data to a pickle file to be used as cache.

	Params: filename, python object
	'''
	outfd = open(filename, 'wb')
	pickle.dump(data, outfd)
	outfd.close()

def loadCache(filename):
	'''
	Loads data from cache file and returns the data.

	Params: filename

	Returns: python object data
	'''

	# There is a chance the data in the cache file becomes corrupt or is over written by invalid data.
	# If that would happen, it will only be showing invalid data for no more than 60 minutes.
	# At this time I choose not to verify the data in the cache file.

	infd = open(filename, 'rb')
	data = pickle.load(infd)
	infd.close()

	return data

# Weather coniditions are updated once an hour at worldweatheronline.com. Therefore we can cache data for a zip code.
# If the file is older than 60 min, then get fresh data. Otherwise use the cached data.
def getConditions():
	'''
	Wrapper function to loadData() and cacheData().

	Returns: python object data
	'''
	# I chose not to check if cache dir exists because if it doesn't, the script will raise an exception and exit. Then
	# a user can create the cache dir and rerun.
	cachefile = os.path.join('cache', zipcode)
	if os.path.exists(cachefile):
		(_, _, _, _, _, _, _, _, mtime, _) = os.stat(cachefile)

		if (time.time() - mtime) > 3600:
			# Older than 1 hour; get new info
			data = loadData()
			cacheData(cachefile, data)
		else:
			data = loadCache(cachefile)
	else:
		data = loadData()
		cacheData(cachefile, data)

	# No need to print a URL to an icon; this can always be removed if the icon is needed.
	if 'weatherIconUrl' in data['data']['current_condition'][0]:
		del data['data']['current_condition'][0]['weatherIconUrl']

	return data

def printConditions(data):
	print "Current weather conditions for %s" % zipcode
	for k in data['data']['current_condition'][0].keys():
		print "%s: %s" % (k, data['data']['current_condition'][0][k])


if __name__ == '__main__':
	conditions = getConditions()
	printConditions(conditions)