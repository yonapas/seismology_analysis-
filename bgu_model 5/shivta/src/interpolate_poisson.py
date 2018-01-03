import numpy as np
# import matplotlib.pyplot as plt
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
	# line = y_line.split(",") # get data from line in files
	line = y_line # get data from list, not from files

	index = line[0]
	# print index
	lat_long = "{0}_{1}".format(line[1], line[2])
	y_axis = line[3:] #take only values
	# convert to float 
	y_axis = convert_to_float(y_axis)

	#return lat_long, y_axis
	return int(index), y_axis, lat_long


def convert_to_float(data_str):
	for i in range(len(data_str)): data_str[i] = float(data_str[i]) #convert to float
	return data_str

def convert_to_str(data_float):
	for i in range(len(data_float)): data_float[i] = str(data_float[i]) #convert to float
	return data_float


def save_in_file(data, chance, name):
	"""
	the function save data in file
	get all data, include normal data, and interpolate.
	save file as poisson+data
	"""
	output_file = open("../csv_data/{0}_{1}_{2}.csv".format(name, str(chance), time.strftime("%Y%m%d%H%M")), "w")
	# output_file.write("LAT, LNG, AMP\n")
	output_file.write("INDEX, AMP\n")
	for coord in data:
		val = data[coord][0]
		loc = data[coord][1]
		output_file.write("{0}, {1}, {2}\n".format(str(loc).replace("_", ","), str(coord), str(val)))
	output_file.close()


def interpolate(poisson_data, name, saveFiles=False):
	# open poission data
	# data_to_interpolate = open("../csv_data/5_10_413_protoPoisson_Prob201801011010.csv").readlines()
	data_to_interpolate = poisson_data

	headline = data_to_interpolate[0] # take X axis
	del data_to_interpolate[0] # remove from data
	# y_axis = headline.split(",")[3:] # takes only values
	y_axis = headline[3:]  # takes only values
	AMP = convert_to_float(y_axis)

	# interpolate_graph(x_axis, data_to_interpolate)
	x_all_data_21 = {}
	x_all_data_102 = {}
	x_all_data_404 = {}
	counter = 0

	for line in data_to_interpolate:
		# get coordinate + poisson value
		coord, poiss_chances, lat_lng = cord_and_value(line)
		new_poisson = poiss_chances+interpolate_values
		new_poisson = sorted(new_poisson)
		# do interpolate with numpy
		try:
			new_value_21 = interp1d(poiss_chances, AMP)(0.0021)
			x_all_data_21[coord] = [float(new_value_21), lat_lng]
			new_value_102 = interp1d(poiss_chances, AMP)(0.00102)
			x_all_data_102[coord] = [float(new_value_102), lat_lng]
			new_value_404 = interp1d(poiss_chances, AMP)(0.000404)
			x_all_data_404[coord] = [float(new_value_404), lat_lng]
		except:
			counter += 1
			print coord, counter

	# store in dict
	print "\n21\n", len(x_all_data_21)
	print "\n102\n" , len(x_all_data_102)
	print "\n404\n", len(x_all_data_404)

	if saveFiles:
		save_in_file(x_all_data_21, 0.0021, name)
		save_in_file(x_all_data_102, 0.00102, name)
		save_in_file(x_all_data_404, 0.000404, name)




