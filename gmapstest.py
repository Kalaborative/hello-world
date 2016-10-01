# First we import our googlemaps module
# so we can communicate with the API.
import googlemaps

# Set your API key to a variable
key = "AIzaSyCshp5LS_bmxQR6-vqGP6f5apFpw9vmVrQ"

# connect to the Google Maps API using that key
g = googlemaps.Client(key=key)

# Define our beginning and ending locations
startpl = "San Francisco"
stoppl = "Los Angeles"

# Using the directions method, we use our variables as the parameters.
result = g.directions(origin=startpl, destination=stoppl)

# Because the result is a LIST, we want to remove it
# so that we are working with a DICT instead.
maps = result[0]

# Use a for-loop to iterate through the dict
with open('trip.html','wb') as code: # We can save the code to an HTML file
	for gmap in maps['legs']:
		for step in gmap['steps']:
			code.write(step['html_instructions'])

code.close()
# Make sure to close your file so you can save it!