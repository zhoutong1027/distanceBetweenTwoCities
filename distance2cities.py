import googlemaps
import csv
from datetime import datetime

# Replace 'YOUR_KEY' with an actual API key
gmaps = googlemaps.Client(key='YOUR_KEY')
origins = []

# Read from csv
with open('cities.csv', 'rb') as f:
	reader = csv.reader(f)
	origins = list(reader)
	# for debugging
	print (len(origins))

destinations = origins

# for debugging
print (len(destinations))

# Distances
my_distances = []
for i in range(len(origins)):
	for j in range(len(destinations)):
		my_distance_dict = gmaps.distance_matrix(origins[i], destinations[j], units="imperial")
		the_distance = my_distance_dict['rows'][0]['elements'][0]['distance']['text']
		if(the_distance == "1 ft"):
			the_distance = "0 mi"
		# for debugging
		print (the_distance)
		my_distances.append(the_distance)

# open a file for writing
with open('twoCities.csv', 'w') as resultFile:
	wr = csv.writer(resultFile)
	wr.writerow(my_distances)


