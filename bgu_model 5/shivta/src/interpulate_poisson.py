import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import settings
import time


interpolate_values = settings.interapt_values

def cord_and_value(y_line):
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
	head = convert_to_str(list(head))
	output_file = open("../csv_data/Poisson_Prob_Interpulate{0}"
		.format(time.strftime("%Y%m%d%H%M")), "w")
	output_file.write("AMP, LAT, LNG,"+', '.join(list(head))+"\n")
	for coord in data:
		val = convert_to_str(list(data[coord]))
		output_file.write("Poisson_Prob, {0}".format(str(coord).replace("_", ","))+', '.join(list(val))+"\n")
	output_file.close()



def interpulate_graph(x_axis, data_to_interpulate):
	
	# make new list with more values
	x_new = np.arange(min(x_axis), max(x_axis)+ 0.02, 0.02) 

	# print len(x_axis)

	y_axis_data = {} # store all data in dict
	for line in data_to_interpulate:
		coord, y_axis = cord_and_value(line)
		
		# interpulate to new function
		inter = interp1d(x_axis, y_axis)(x_new)
		inter_cubic = interp1d(x_axis, y_axis, kind='cubic')(x_new)

		plt.plot(x_new, inter, "-", x_new, inter_cubic, "--", x_axis, y_axis, "*")
		plt.legend(["data", "interp1d", "cubic"], loc="best")
		y_axis_data[coord] = y_axis, inter, inter_cubic

	#print y_axis_data
	# interpulate:
	plt.show()

data_to_interpulate = open("../csv_data/Poisson_Prob201711031036.csv").readlines()

headline = data_to_interpulate[0] # take X axis
del data_to_interpulate[0] # remove from data
x_axis = headline.split(",")[3:] # takes only values
convert_to_float(x_axis)

# interpulate_graph(x_axis, data_to_interpulate)
full_AMP = x_axis+interpolate_values
y_all_data = {}

for line in data_to_interpulate:
	coord, y_axis = cord_and_value(line)
	new_value = np.interp(interpolate_values, x_axis, y_axis)
	full = zip(full_AMP, y_axis+list(new_value))
	full = sorted(full, key=lambda point: point[0])
	X, Y = zip(*full)
	y_all_data[coord] = Y

save_in_file(X, y_all_data)




