import numpy as np
import utm
from common import orgenize_line


config = {}
execfile("../shivta.conf", config)
grid_csv = config['grid_csv']
input_file = config['input']
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
	return lat_cor, lng_cor, int(num)


def create_input(data):
	"""
	thit function create input file to Haz45, 
	according tamplate you can find in folder. 
	the function run over each cordinate, and create lines in input file.
	"""
	number_of_sites = len(data)
	
	


header = orgenize_line.orgenize(first_line)

csv_data = open(grid_csv, "r").readlines()
del csv_data[0]
cord_data = []

for line in csv_data:
	lat, lng, num = from_utm(line)
	cord_data.append([lat, lng, num])

create_input(cord_data)