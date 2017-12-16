from math import sqrt


def tri_num_factors(n):
	"""
	Returns: First triangle number with more than n factors
	"""
	tri = 3
	diff = 3
	factors=2

	while factors <= n:
		#We don't need to repeatedly calculate factors of 1 and tri
		factors = 2

		#Move onto next triangle number
		tri += diff
		diff += 1

		#We just need to go up to the last integer before the square root and and double count each (since a factor less than sqrt(tri) corresponds to a factor greater than sqrt(tri))
		for i in xrange(2,int(sqrt(tri)+1)):
			if tri%i==0:
				factors += 2
	return tri


print tri_num_factors(500)