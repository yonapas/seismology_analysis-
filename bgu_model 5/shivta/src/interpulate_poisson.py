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
	output_file = open("../csv_data/Poisson_Prob_Interpolate{0}"
		.format(time.strftime("%Y%m%d%H%M")), "w")
	output_file.write("AMP, LAT, LNG,"+', '.join(list(head))+"\n")
	for coord in data:
		val = convert_to_str(list(data[coord]))
		output_file.write("Poisson_Prob, {0}".format(str(coord).replace("_", ","))+', '.join(list(val))+"\n")
	output_file.close()



def interpolate_graph(x_axis, data_to_interpolate):
	"""
	this function make graph of interpolation
	NOT depented in "interpolate_values"
	do interpolate for all range.
	"""
	
	# make new list with more values
	x_new = np.arange(min(x_axis), max(x_axis)+ 0.02, 0.02) 

	# print len(x_axis)

	y_axis_data = {} # store all data in dict
	for line in data_to_interpolate:
		coord, y_axis = cord_and_value(line)
		
		# interpolate to new function
		inter = interp1d(x_axis, y_axis)(x_new)
		inter_cubic = interp1d(x_axis, y_axis, kind='cubic')(x_new)

		plt.plot(x_new, inter, "-", x_new, inter_cubic, "--", x_axis, y_axis, "*")
		plt.legend(["data", "interp1d", "cubic"], loc="best")
		y_axis_data[coord] = y_axis, inter, inter_cubic

	#print y_axis_data
	# interpolate:
	plt.show()

# open poission data 
data_to_interpolate = open("../csv_data/Poisson_Prob201711031036.csv").readlines()

headline = data_to_interpolate[0] # take X axis
del data_to_interpolate[0] # remove from data
x_axis = headline.split(",")[3:] # takes only values
convert_to_float(x_axis)

# interpolate_graph(x_axis, data_to_interpolate)
full_AMP = x_axis+interpolate_values
y_all_data = {}

for line in data_to_interpolate:
	# get coordinate + poisson value
	coord, y_axis = cord_and_value(line)
	# do interpolate with numpy
	new_value = np.interp(interpolate_values, x_axis, y_axis)
	# sort data 
	full = zip(full_AMP, y_axis+list(new_value))
	full = sorted(full, key=lambda point: point[0])
	X, Y = zip(*full)

	# store in dict
	y_all_data[coord] = Y

save_in_file(X, y_all_data)




