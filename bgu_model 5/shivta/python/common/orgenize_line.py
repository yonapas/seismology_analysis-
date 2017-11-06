
def orgenize(header_ori, lat=None, lng=None):

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