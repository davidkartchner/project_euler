"""
David Kartchner
Project Euler Problem 21
May 12, 2016
"""

def d(n):
	divisor_sum=0
	for i in xrange(1, n//2+1):
		if n%i==0:
			divisor_sum+=i
	return divisor_sum

def create_amicable_dict(n):
	amic_dict = {0:0, None:0}
	for i in xrange(1, n+1):
		if i%1000==0:
			print i
		amic_dict[i] = d(i)
	return amic_dict

def sum_amicable_numbers(n):
	amic_sum = 0
	amic_dict = create_amicable_dict(n)
	#print amic_dict
	for i in xrange(1, n+1):
		#if i%100==0:
			#print i
		if amic_dict[i]>n:
			continue
		if i==amic_dict[amic_dict[i]]:
			if i!=amic_dict[i]:
				amic_sum+=i
	return amic_sum


if __name__ == '__main__':
	print sum_amicable_numbers(10000)