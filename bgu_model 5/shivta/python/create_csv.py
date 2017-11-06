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

global value
global del_value

# exe config file 
config = {}
execfile("shivta.conf", config)
header_ori = config['header'] 
value = config['value'] # poisson or something else
location = config['cor']
del_value = config['nonrelevent']


def orgenize_line(header_ori, lat=None, lng=None):

	"""
	this function get line from 'out' file, 
	and reorganize it.
	remove space and add lat-lng value
	return one list, contian line
	"""

	ori_list = header_ori.split(" ")
	if lat and lng:
		ori_list[3], ori_list[4] = lat, lng
	relist = []
	# clean all space:
	for val in ori_list:
		if val != "":
			relist.append(val)

	# clean new line if exist
	relist[-1] = relist[-1].split("\r")[0].split("\n")[0]
	return relist


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


def list_to_array(data, l):
	"""
	this function get data (in lists)
	and convert it to csv file.
	remove non rellevent parameters
	"""
	a = np.array(data)
	a.reshape((len(data), l))

	if del_value:
		a = clean_array(a, data[0])
	 
	date = time.strftime("%Y%m%d%H%M")

	# save csv file, in csv folder. add data to title 
	np.savetxt('../csv_data/'+value+date+".csv", a, delimiter=",", fmt='%s')
	print "create csv file"

# --------------------------------------- #
# start script here!                      #


# define header line  to csv and store in data
firs_line = orgenize_line(header_ori, "LAT", "LONG")
data = [firs_line]

lat, lng = 0, 0

# take all "out" file
files_name = glob.glob('../outfile/*.out')

# run for all out file
for item in files_name:
	
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
			cord = orgenize_line(line)
			lat, lng = cord[-1], cord[-2]
			# del new line from lat
			lat = lat.split("\n")[0]
			site_num = cord[1]
		
		if value in line:
			# find one value in file
			line = orgenize_line(line, lat, lng)
			data.append(line)
	out_read.close()
l = len(data[-1])
list_to_array(data, l)

