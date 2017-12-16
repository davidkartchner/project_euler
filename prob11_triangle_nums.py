import numpy as np 


def tri_num_factors(n):
	"""
	Returns: First triangle number with more than n factors
	"""
	#initialize arrays of factors of n and n+1
	a = 0
	b = 0
	#index of triangle number
	k = 0
	factors = 0

	#recall that the nth triangle number is given by n*(n+1)/2
	while factors < 501:
