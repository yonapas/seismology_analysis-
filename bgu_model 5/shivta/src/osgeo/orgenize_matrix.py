import numpy as np 

grid = open("grid_israel_2_2_km.csv", "r").readlines()
new_grig_file = open("new_2_2_km_.csv", "w")

# del grid[0] # del header
new_grig = []
del grid[0]

for line in grid:
	new_line = line.split(",")
	# print new_line
	lat, lng, num, flag = new_line[0], new_line[1], new_line[2], int(new_line[3])
	if flag > 0 and int(num) > 18378:
		new_grig.append(line)


new_grig_file.write("lat, lng, num, flag\n")
for l in new_grig:

	new_grig_file.write(l)

new_grig_file.close()
print "done"