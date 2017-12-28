import numpy as np

# (85, 28) - shape 5 km
# (221, 88) - shape 2 km


def indices(list, filtr=lambda x: bool(x)):
	return [i for i, x in enumerate(list) if filtr(x)]


full_csv_data = open("osgeo/grid_israel_2_2_km.csv", "r").readlines()
amp_csv_data = open("../csv_data/Poisson_Prob_Interpolate_2_0.000404_201712282220.csv", 'r').readlines()

del full_csv_data[0], amp_csv_data[0]

l_f = len(full_csv_data)
l_bor = len(amp_csv_data)

print l_f, "full"
print l_bor, "border"

all_num_full = []
all_lat_full = []
all_lng_full = []

for line in full_csv_data:
	line = line.split(",")
	num , lat, lng = line[2], line[0], line[1]
	all_num_full.append(int(num))
	all_lat_full.append(float(lat))
	all_lng_full.append(float(lng))

for val in amp_csv_data:
	val = val.split(",")
	index, amp = int(val[0]), float(val[1])
	i = all_num_full.index(index)
	all_num_full[i] = amp

out = indices(all_num_full, lambda x: x > 1)

for i in out:
	# all_num_full[i] = None
	all_num_full[i] = 0

# make value mat
full_array = np.asarray(all_num_full)
full_grig_amp = full_array.reshape(221, 88)

# make lat matrix
lat_array = np.asarray(all_lat_full)
full_grid_lat = lat_array.reshape(221, 88)

# make lng matrix
lng_array = np.asarray(all_lng_full)
full_grid_lng = lng_array.reshape(221, 88)

print len(full_grig_amp), "amp"
print len(full_grid_lat), "lat"
print len(full_grid_lng), "lng"

out_file_xyz = open("../outfile/data_2_2_0.0004.txt", "w")
for i in range(len(all_num_full)):
	out_file_xyz.write("{0}, {1}, {2}\n".format(str(all_lng_full[i]), str(all_lat_full[i]), str(all_num_full[i])))

out_file_xyz.close()