import numpy as np 

A = []
f = open('p13_nums.txt','r')
for line in f:
	A.append([int(i)for i in line.strip()])
A = np.array(A)

digits = []
temp = 0
for i in xrange(49,-1,-1):
	col_sum = np.sum(A[:,i])+temp
	digits.insert(0,col_sum%10)
	temp = col_sum//10
	if i==0:
		digits.insert(0, (col_sum//10)%10)
		if col_sum//100>0:
			digits.insert(0, col_sum//100)
for i in xrange(10):
	print digits[i]