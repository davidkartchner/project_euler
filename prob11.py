import numpy as np


#n is number of entries to multiply together
def gridmax(filename, n):
	"""
	Find maximum product of n adjacent numbers in a square grid

	Parameters:
		filename: text file containing grid
		n: number of multiply in grid
	Returns:
		gmax: maximum product in grid
	"""
	#Read in file and convert to numpy array
	#File should be a m x m grid of numbers
	grid = []
	gmax = -np.inf
	max
	f = open(filename, 'r')
	for line in f:
		row = [int(i) for i in line.split()]
		grid.append(row)
	grid = np.array(grid)
	m = grid.shape[0]
	for i in xrange(m):
		for j in xrange(m-n):
			#Look at vertical sequences
			if np.prod(grid[j:j+n,i])>gmax:
				gmax = np.prod(grid[j:j+n,i])

			#Horizontal sequences
			if np.prod(grid[i,j:j+n])>gmax:
				gmax = np.prod(grid[i,j:j+n])

			#Diagonal sequences
			prod1 = 1
			prod2 = 1
			if i <m-n:
				for k in xrange(n):
					prod1 *=grid[i+k, j+k]
					prod2 *=grid[i+n-k, j+k]
				if prod1>gmax:
					gmax=prod1
				if prod2>gmax:
					gmax=prod2
	return gmax


print gridmax('grid_prob_11.txt',4)