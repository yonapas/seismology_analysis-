import utm
import time
import settings


grid_csv = settings.grid_csv
input_template = settings.input_template
final_input = settings.finel_input
first_line = settings.cordinate_line

global israel_latt
global israel_num

israel_latt = 'R'
israel_num = 36

def from_utm(data):
	arr = data.split(",")
	lat_u, lng_u, num = float(arr[0]), float(arr[1]), float(arr[2])
	cordinate = utm.to_latlon(lat_u, lng_u, israel_num, israel_latt)
	lat_cor, lng_cor = cordinate[0], cordinate[1]
	return round(lat_cor, 6), round(lng_cor, 6), int(num)


def save_input(data):
	date = time.strftime("%Y%m%d%H%M")
	finel = open(final_input+date+".inp", 'w')

	for line in data:
		# if type(line) == list:
			# print line
			#line = ' '.join(line)
		finel.write(line)
	finel.close()
	print "create input file"


def create_input(data, input_file):
	"""
	thit function create input file to Haz45, 
	according tamplate you can find in folder. 
	the function run over each cordinate, and create lines in input file.
	"""
	number_of_sites = len(data)
	finput = open(input_file, 'r').readlines()
	finput[-1] = finput[-1].replace('1', str(number_of_sites))
	# print header
	all_site_data =[]

	for site in data:
		title = ''.join(first_line)
		_lat, _lng = str(site[0]), str(site[1])
		index = str(site[2]).split("\n")[0]
		tit = title.replace("LNG", _lng).replace("LAT", _lat)
		all_site_data.append(tit)
		# print all_site_data , "\n\n"
		for i in range(0,6):
			all_site_data.append("out_{0}_{1}.out\n".format(i, index))


	finput = finput+all_site_data
	# print finput
	save_input(finput)


csv_data = open(grid_csv, "r").readlines()
del csv_data[0]
cord_data = []

for line in csv_data:
	# lat, lng, num = from_utm(line)
	line = line.split(",")
	lat, lng, num = line[0], line[1], line[2]
	cord_data.append([str(lat), str(lng), num])

create_input(cord_data, input_template)

