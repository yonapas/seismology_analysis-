import numpy as np
import utm
# from src.common import orgenize_line
from common import orgenize_line
import time


config = {}
execfile("shivta.conf", config)
grid_csv = config['grid_csv']
input_template = config['input_template']
finel_input = config['finel_input']
first_line = config['cordinate_line']

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
	finel = open(finel_input+date+".int", 'w')

	for line in data:
		finel.write(line)
	print "create input file"



def create_input(data, input_file):
	"""
	thit function create input file to Haz45, 
	according tamplate you can find in folder. 
	the function run over each cordinate, and create lines in input file.
	"""
	number_of_sites = len(data)
	finput = open(input_file, 'r').readlines()
	finput[-2] = finput[-2].replace('1', str(number_of_sites))
	print header
	all_site_data =[]
	for site in data:
		title = header
		lat, lng = site[0], site[1]
		title[0], title[1] = lng, lat
		all_site_data.append(title)
		for num in range(1,6):
			all_site_data.append("out_{0}_{1}_{2}.out".format(num, lng, lat))
	print len(all_site_data)
	finput = finput+all_site_data
	save_input(finput)


header = orgenize_line.orgenize(first_line)

csv_data = open(grid_csv, "r").readlines()
del csv_data[0]
cord_data = []

for line in csv_data:
	lat, lng, num = from_utm(line)
	cord_data.append([lat, lng, num])

create_input(cord_data, input_template)