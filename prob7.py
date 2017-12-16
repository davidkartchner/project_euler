import numpy as np


#Find largest product of n consecutive digits of a big numbe
def largest_prod(filename, n):
#Filename is name of file containing large number
#n is number of consecutive digits to multiply
	string = ''
	f = open(filename, 'r')
	for line in f:
		string = string + line.strip()

	string = np.array(string.split('0'))
	prod = 1

	for i in xrange(len(string)):

		if len(string[i])>=n:
			for j in xrange(1+len(string[i])-n):
				num = 1
				a = string[i][j:j+n].split()

				for k in xrange(n):
					num*=int(a[0][k])
				if num>prod:
					prod = num
	'''

	for j in xrange(len(string)-n):
		num = 1
		a = string[j:j+n].split()
		print a
		for k in xrange(n):
			num*=int(a[0][k])
		if num>prod:
			prod = num
	'''
	return prod

print largest_prod('big_num.txt', 4)
print largest_prod('big_num.txt', 13)


