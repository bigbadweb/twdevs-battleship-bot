import urllib2, random, json


apitoken = ''
baseurl = 'https://battleships.allsecuredomains.com/api/v1/'

def main():

	botname = "battle-bott-1e"

	mapstobuild = 2
	maps  = []
	payload = { "bot_name" : None, "maps" : None}
	payload['bot_name'] = botname
	payload['maps'] = maps
	i  = 0
	while i < mapstobuild:

		ships = generateMap()
		maps.append(ships)
		i +=1


	# print json.dumps(payload, indent=4)

	data = postMaps(payload)
	if data:
		# start

		print data
		print "posted"




def postMaps(payload):
	# print baseurl
	req = urllib2.Request(baseurl + 'upload_maps')
	req.add_header('Authorization', 'Token ' + apitoken)
	req.add_header('Content-Type', 'application/json')
	req.add_data(json.dumps(payload, indent=4))
	response = urllib2.urlopen(req)
	data = json.reads(response.read())

	return data

def generateMap():

	# ships
	lengths = [5,4,3, 3,2,2]
	directions = ['horizontal', 'vertical']


	alpha  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
	xcoords = range(0, 9)
	ycoords = range(0, 9)

	maps = {"ships" : []}

	for length in lengths:
		## pick a direction
		direction = directions[random.randint(0, 1)]

		xmax = 9
		ymax = 9

		# avoid going off the map
		if direction == 'horizontal':
			xmax = xmax - length
		else:
			ymax = ymax - length

		x = random.randint(0, xmax)
		y = random.randint(0, ymax)

		# avoid overlap... hard
		shipcoords = {
						"size" : length,
						"position" : str(alpha[x]) + str(y),
						"direction" : str(direction)
					}

		maps['ships'].append(shipcoords)

	return maps



if __name__ == "__main__":
    main()
