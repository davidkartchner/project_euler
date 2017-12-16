def sum_square_diff(n):
	#sum of squares from 1 to n
	square_sum = (n*(n+1)*(2*n+1))/6

	#square of sum of numbers 1 through n
	sum_squared = (n**2*(n+1)**2)/4
	return sum_squared-square_sum

print sum_square_diff(10)
print sum_square_diff(100)