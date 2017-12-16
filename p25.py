"""
David Kartchner
Project Euler Problem 25
1000 digit Fibonacci Number
May 17, 2016
"""

f1 = 1
f2 = 1
iters = 2
while len(str(f2))<1000:
	iters += 1
	temp = f1+f2
	f1=f2
	f2=temp

	if iters%1000==0:
		print len(str(f2))
print "Index of first 1000-digit Fibonacci number:", iters