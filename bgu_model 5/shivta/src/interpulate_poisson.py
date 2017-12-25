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


def save_in_file(data, chance):
	"""
	the function save data in file
	get all data, include normal data, and interpolate.
	save file as poisson+data
	"""
	output_file = open("../csv_data/Poisson_Prob_Interpolate_{0}_{1}.csv"
		.format(str(chance), time.strftime("%Y%m%d%H%M")), "w")
	output_file.write("LAT, LNG, AMP\n")
	for coord in data:
		val = data[coord]
		output_file.write("{0}, {1}\n".format(str(coord).replace("_", ","), str(val)))
	output_file.close()


# open poission data 
data_to_interpolate = open("../csv_data/Poisson_Prob_data_5_5km.csv").readlines()

headline = data_to_interpolate[0] # take X axis
del data_to_interpolate[0] # remove from data
y_axis = headline.split(",")[3:] # takes only values
AMP = convert_to_float(y_axis)


# interpolate_graph(x_axis, data_to_interpolate)
x_all_data_21 = {}
x_all_data_102 = {}
x_all_data_404 = {}
counter = 0

for line in data_to_interpolate:
	# get coordinate + poisson value
	coord, poiss_chances = cord_and_value(line)
	new_poisson = poiss_chances+interpolate_values
	new_poisson = sorted(new_poisson)
	# do interpolate with numpy
	try:
		new_value_21 = interp1d(poiss_chances, AMP)(0.0021)
		x_all_data_21[coord] = float(new_value_21)
		new_value_102 = interp1d(poiss_chances, AMP)(0.00102)
		x_all_data_102[coord] = float(new_value_102)
		new_value_404 = interp1d(poiss_chances, AMP)(0.000404)
		x_all_data_404[coord] = float(new_value_404)
	except:
		counter += 1




	# sort data
	#full = zip(new_poisson, new_value)
	#full = sorted(full, key=lambda point: point[0])
	# print full
	#X, Y = zip(*full)

	# print X


	# store in dict
print "\n21\n", len(x_all_data_21)
print "\n102\n" , len(x_all_data_102)
print "\n404\n", len(x_all_data_404)

# print x_all_data_21
# save_in_file(x_all_data_21, 0.0021)
save_in_file(x_all_data_102, 0.00102)
save_in_file(x_all_data_404, 0.000404)



