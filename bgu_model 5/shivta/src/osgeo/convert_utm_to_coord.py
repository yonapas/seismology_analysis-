import utm

utm_file ='grid_2_2_km_utm.csv'
coord_file = "grid_israel_2_2_km.csv"

israel_latt = 'R'
israel_num = 36


def utm_to_lat_lng(infile, outfile):
	utm_data = open(infile, 'r').readlines()
	coordi_file_out = open(outfile, 'w')
	coordi_file_out.write("lat,long,name\n")
	del utm_data[0]

	for line in utm_data:
		line = line.split(',')
		lat, lng, id = float(line[0]), float(line[1]), line[2]
		coor = utm.to_latlon(lat, lng, israel_num, israel_latt)
		coordi_file_out.write(str(coor[0])+","+str(coor[1])+","+id)

	coordi_file_out.close()
	print "done"

def lat_lng_to_utm(infile, outfile):
	print "lat long to utm"
	coord_data = open(infile, "r").readlines()
	del coord_data[0]
	utm_out = open(outfile, "w")
	# utm_out.write("utm\n")

	for line in coord_data:
		line = line.split(",")
		lat, lng, id, amp = float(line[0]), float(line[1]), line[2], line[3]
		u = utm.from_latlon(lat, lng)
		amp = amp.split("\n")[0]
		print u
		utm_out.write("{0}, {1}, {2}, 36, R, {3}\n".format(id, str(u[0]), str(u[1]), amp))



lat_lng_to_utm("../../csv_data/GII_413Klar_CB08_0.000404.csv", "utm_GII_413Klar_CB08_0.000404.txt")
