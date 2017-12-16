"""
David Kartchner
Project Euler Problem 15 solution
May 11, 2016
"""
import sys


sys.setrecursionlimit(9000)


path_lengths = {(1,0):1, (0,1):1, (1,1):2}
def lattice_paths(n,m):
	if m==0 or n==0:
		return 1
	if (n,m) in path_lengths:
		return path_lengths[(n,m)]
	
	else:
		path_sum = lattice_paths(n-1,m) + lattice_paths(n, m-1)
		path_lengths[(n,m)] = path_sum
		path_lengths[(m,n)] = path_sum
		return path_sum


print lattice_paths(20,20)
#print path_lengths