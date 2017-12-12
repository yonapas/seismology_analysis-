import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import settings
import time

# value to do interpolate
interpolate_values = settings.interapt_values

def cord_and_value(y_line):
	"""
	this function get line , and return coordinate 
	and convert rest value to float
	"""

	line = y_line.split(",")
	lat_long = "{0}_{1}".format(line[1], line[2])
	y_axis = line[3:] #take only values
	# convert to float 
	y_axis = convert_to_float(y_axis)

	return lat_long, y_axis


def convert_to_float(data_str):
	for i in range(len(data_str)): data_str[i] = float(data_str[i]) #convert to float
	return data_str

def convert_to_str(data_float):
	for i in range(len(data_float)): data_float[i] = str(data_float[i]) #convert to float
	return data_float


def save_in_file(head, data):
	"""
	the function save data in file
	get all data, include normal data, and interpolate.
	save file as poisson+data
	"""
	head = convert_to_str(list(head))
	output_file = open("../csv_data/Poisson_Prob_Interpolate{0}.csv"
		.format(time.strftime("%Y%m%d%H%M")), "w")
	output_file.write("AMP, LAT, LNG,"+', '.join(list(head))+"\n")
	for coord in data:
		val = convert_to_str(list(data[coord]))
		output_file.write("Poisson_Prob, {0}".format(str(coord).replace("_", ","))+', '.join(list(val))+"\n")
	output_file.close()



# open poission data 
data_to_interpolate = open("../csv_data/Poisson_Prob201711031036.csv").readlines()

headline = data_to_interpolate[0] # take X axis
del data_to_interpolate[0] # remove from data
y_axis = headline.split(",")[3:] # takes only values
AMP = convert_to_float(y_axis)


# interpolate_graph(x_axis, data_to_interpolate)
x_all_data = {}

for line in data_to_interpolate:
	# get coordinate + poisson value
	coord, poiss_chances = cord_and_value(line)
	new_poisson = poiss_chances+interpolate_values
	new_poisson = sorted(new_poisson)
	# do interpolate with numpy
	new_value = interp1d(poiss_chances, AMP)(new_poisson)

	# sort data 
	full = zip(new_poisson, new_value)
	full = sorted(full, key=lambda point: point[0])
	# print full
	X, Y = zip(*full)

	print X #

	# store in dict
	x_all_data[coord] = X

#save_in_file(X, y_all_data)




