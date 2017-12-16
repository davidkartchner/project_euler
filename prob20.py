"""
David Kartchner
Project Euler Problem 20
May 12, 2016
"""

def n_factorial(n):
	#make sure n is an int
	n = int(n)
	if n==0:
		return 1
	elif n==1:
		return 1
	elif n<0:
		raise ValueError("Can't take factorial of negative number")
	else:
		return n*n_factorial(n-1)


hundred_factorial =  str(n_factorial(100))
print sum([int(i) for i in hundred_factorial])