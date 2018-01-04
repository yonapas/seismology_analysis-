"""
this script written by Yona Pashchur, at Nov 2017.
the script take all out-file in "outfile" folder and find relevant data from it.
data define in config file.
the script made cav file. and save it in csv_data folder

if somethings goes wrong please let me know :)
"""

import numpy as np
import time
import glob
from common import orgenize_line
import settings

global value
global del_value


value = settings.value  # poisson or something else
location = settings.cor
del_value = settings.nonrelevent


def clean_array(array, head):
	"""
	this function clean array by configure non relevent element 
	get - array 
	and his header
	find non relevent index, and delete colums from array
	return - clean array
	"""

	# define non relevent element
	elements = del_value.split(",")
	colum_to_del = []

	# find the index in header.
	for e in elements:
		if e in head:
			index = head.index(e)
			colum_to_del.append(index)

	# del the non relevant element from all matrix
	b = np.delete(array, colum_to_del, axis=1)
	return b


def list_to_array(data, l, param, save):
	"""
	this function get data (in lists)
	and convert it to csv file.
	remove non rellevent parameters
	"""
	a = np.array(data)
	a.reshape((len(data), l))
	a = clean_array(a, data[0])
	date = time.strftime("%Y%m%d%H%M")

	if save:
		# save csv file, in csv folder. add data to title
		np.savetxt('../csv_data/{0}_{1}_{2}.csv'.format(param, value, date), a, delimiter=",", fmt='%s')
		print "create csv file"
	a_list = a.tolist()
	return a_list
# --------------------------------------- #
# start script here!                      #


# define header line  to csv and store in data
def create(folder, parameter, writeToFile=False):

	lat, lng = 0, 0

	# take all "out" file
	files_name = glob.glob('../{0}/out_4_*.out'.format(folder))
	header = None

	if len(files_name)> 0:

		one_file = open(files_name[0], "r").readlines()
		for line in one_file:
			if "AMP" in line:
				header = line
	else:
		print "No OUT_4 files found, please check again your settings,\n and make shore your src file in right path"
		return None

	if header:
		firs_line = orgenize_line.orgenize(header, "LAT", "LONG")
		data = [firs_line]
	else:
		print "Error With Fiels, can't find AMP values from out_4"

	# run for all out file
	for item in files_name:

		# find site index for grid
		site_num = item.split("_")[-1].split(".")[0]

		# open file:
		out_read = open(item, 'r')
		lines = out_read.readlines()
		# find value in line, and store it
		for line in lines:
			if location in line:

				# find lat-long in site
				# find site number (case few site in one out-file)
				# for now - do nothing with site number #
				cord = line.split(" ")
				cord = orgenize_line.orgenize(line)
				lat, lng = cord[-1], cord[-2]

			if value in line:
				# find one value in file
				line = orgenize_line.orgenize(line, lat, lng)
				# set index of site
				line[0] = site_num
				data.append(line)
		out_read.close()
	l = len(data[-1])
	# print data[0]
	clean_data = list_to_array(data, l, parameter, writeToFile)
	# print clean_data
	return clean_data

create("outfile", "test")


