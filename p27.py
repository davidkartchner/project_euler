"""
David Kartchner
Project Euler Problem 27--Quadratic Primes
May 21, 2016
"""

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



def quadratic_primes():
    max_seq = 0
    best_a=1
    best_b=41
    possible_b = primes_below_n(1000)
    divisors = primes_below_n(2000)
    for a in xrange(-1000,1001):
        #if a%10==0:
            #print a
        for b in possible_b:
            n=0
            prime=True
            while prime:
                num = n**2 + a*n + b
                for i in divisors:

                    if num%i == 0 and num!=i:
                        prime=False
                if prime:
                    n+=1
                if n > max_seq:
                    print "New best a and b:", a, b
                    print "New best n:", n
                    max_seq = n
                    best_a = a
                    best_b = b
    print "Best Product:", best_b*best_a

if __name__ == '__main__':
    quadratic_primes()
