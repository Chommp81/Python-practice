import urllib
import json

serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

api_key = #api_key goes here



while True:
	address = raw_input("Choose a location: ")
	if len(address) < 1: break

	url = serviceurl + urllib.urlencode({
		'key':api_key, 
		'address':address
		})
	print "Retrieving %s ......." % (url)

	uh = urllib.urlopen(url)
	data = uh.read()

	print "Retrieved %s characters" % (len(data))
	
	info = json.loads(data)

	lat = info['results'][0]['geometry']['location']['lat']
	lng = info['results'][0]['geometry']['location']['lng']
	formatted_address = info['results'][0]['formatted_address']

	print formatted_address
	print "The latitude is %s and the longtitude is %s" % (lat,lng)


