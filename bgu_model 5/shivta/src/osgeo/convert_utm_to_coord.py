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
	coord_data = open(infile, "r").readlines()
	utm_out = open(outfile, "w")
	utm_out.write("utm\n")

	for line in coord_data:
		line = line.split(",")
		lat, lng, id = float(line[0]), float(line[1]), line[2]
		u = utm.from_latlon(lat, lng)
		utm_out.write("{0}, {1}, 36, S\n".format(str(u[0]), str(u[1])))


lat_lng_to_utm("../../csv_data/data_5_5_0.0021.txt", "utm_5_5_0.0021.csv")
