import numpy as np



#find all primes under n
def primes_below_n(n):
	primes = np.array([i for i in xrange(2, n+1)])
	k = int(np.sqrt(n))
	#we only need to use primes less than sqrt n to eliminate composite numbers
	seive = np.array([i for i in xrange(2, k+1)])
	#j is indexing number
	j = 0

	while j < len(seive):
		primes = primes[(primes <= seive[j])|(primes%seive[j] != 0)]
		seive = seive[(seive%seive[j]!=0)|(seive <= seive[j])]

		j+=1
	return primes

#finds least common multpile of all numbers leq n
def lcm(n):
	primes = primes_below_n(n)
	num = 1
	for i in primes:
		k = i
		while k*i < n:
			k*=i
		num*=k
	return num

print lcm(10)
print lcm(20)