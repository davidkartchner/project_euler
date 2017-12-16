import numpy as np


#1000000=2000a+2000b-2ab
def pathagorean_triple():
	for a in xrange(1,1000):
		for b in xrange(1,1000):
			if 2000*(a+b) - 2*a*b > 1000000:
				break
			elif 2000*(a+b) - 2*a*b == 1000000:
				c = (1000-a-b)
				return a, b, c, a*b*c


print pathagorean_triple()