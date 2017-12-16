"""
David Kartchner
Project Euler Problem 23
Abundant Numbers
May 13, 2016
"""

def d(n):
	divisor_sum=0
	for i in xrange(1, n//2+1):
		if n%i==0:
			divisor_sum+=i
	return divisor_sum

def ab_num_sums(n):
	ab_nums = []
	ab_num_sums = []
	for i in xrange(1, n+1):
		if i%1000==0:
			print i
		if d(i) > i:
			ab_nums.append(i)
	print ab_nums

	for i in ab_nums:
		for j in ab_nums:
			ab_num_sums.append(i+j)


	return set(ab_num_sums)

def main():
	imp_num_sum = 0
	bad_nums = ab_num_sums(28123)

	for i in xrange(1,28124):
		if i not in bad_nums:
			imp_num_sum+=i
		else:
			print i
		
	print imp_num_sum


if __name__ == '__main__':
	main()
