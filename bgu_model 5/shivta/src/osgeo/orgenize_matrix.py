import numpy as np 

grid = open("grid_5_5_km.csv").readlines()

# del grid[0] # del header

a = np.matrix(grid)
b = a.reshape((35, 84))
# print b[:,0]
print b[0, 46]

#46 to 5_5 KM
