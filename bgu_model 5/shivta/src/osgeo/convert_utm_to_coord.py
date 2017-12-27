import utm

utm_file ='grid_2_2_km_utm.csv'
coord_file = "grid_israel_2_2_km.csv"

israel_latt = 'R'
israel_num = 36

utm_data = open(utm_file, 'r').readlines()
coordi_file_out = open(coord_file, 'w')
coordi_file_out.write("lat,long,name\n")
del utm_data[0]

for line in utm_data:
	line = line.split(',')
	lat, lng, id = float(line[0]), float(line[1]), line[2]
	coor = utm.to_latlon(lat, lng, israel_num, israel_latt)
	coordi_file_out.write(str(coor[0])+","+str(coor[1])+","+id)

coordi_file_out.close()
print "done"