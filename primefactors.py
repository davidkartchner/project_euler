import numpy as np
from math import sqrt
import time

def seive(n):
	nums = np.array([i for i in xrange(2, n)])
	seive_primes = nums[nums<=sqrt(n)]
	i=0
	
	while i < len(seive_primes):
		k = seive_primes[i]
		nums = nums[(nums==k)|(nums%k!=0)]
		seive_primes = seive_primes[(seive_primes==k)|(seive_primes%k!=0)]
		i+=1
	
	return nums


def prime_factors(n):
	primes = seive(int(sqrt(n)))
	i=0
	while i<len(primes) & n>primes[i]:
		while n%primes[i]==0:
			n/=primes[i]
		i+=1
	return n


def find_nth_prime(n):
	k = 1000000
	i=0
	while i < n:
		primes=seive(k)
		i = len(primes)
		k*=10
	return primes[n]

if __name__ == "__main__":
	start = time.time()
	print find_nth_prime(10001)
	print time.time()-start
	

