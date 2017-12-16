import numpy as np

#Find longest Collatz sequence under 1,000,000

#Create Collatz sequences:
def largest_collatz_seq(n):
	#n must be a positive integer

	seq_lengths = {1:1, 2:2}


	for n in xrange(1,n+1):
		if n%1000==0:
			print n
		iters=1
		values = []
		counts = np.array([])
		while n>1:
			if n in seq_lengths:
				counts += seq_lengths[n]
				for i in xrange(len(values)):
					seq_lengths[values[i]] = counts[i]-1
				break
			elif n%2==0:
				values.append(n)
				counts = np.append(counts, np.array([1]))
				#print values
				#print counts
				n /= 2
				counts += 1
				
			else:
				values.append(n)
				counts = np.append(counts, np.array([1]))
				n = 3*n + 1
				counts += 1

	sizes = []
	for i in xrange(1, n+1):
		sizes.append(seq_lengths[i])
	sizes = np.array(sizes)
	#print sizes
	print "Max: ", np.max(sizes)
	print "Maximizing number:", np.argmax(sizes) + 1

largest_collatz_seq(1000000)
