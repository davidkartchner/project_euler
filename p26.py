"""
David Kartchner
Project Euler Problem 26
Repeating Decimals
May 17, 2016
"""

"""
import decimal as d
	
precision = 6000
d.getcontext().prec = precision




def find_string_patterns(n):
	dec_reps = [str(d.Decimal(1)/d.Decimal(k)) for k in xrange(2,n)]
	denoms = range(2,n)
	pat_lengths = []
	iters=2
	for string in dec_reps:
		print "Current Number:", iters
		string = string[2:-1]
		l_str = len(string)
		pat_found=False

		for i in xrange(l_str-2,-1,-1):
			pattern = string[i:-1]
			l_pat = len(pattern)
			

			if string[l_str-l_pat-1:l_str-1]==pattern:

				pat_found=True
				for i in xrange(2,5):
					if string[l_str-i*l_pat-1:l_str-(i-1)*l_pat-1]!=pattern:
						#print "Pattern:", pattern
						#print "String:", string[l_str-i*l_pat-1:l_str-1]
						pat_found=False
			if pat_found:
				print pattern
				pat_lengths.append(l_pat)
				break
		if not pat_found:
			print 0
			pat_lengths.append(0)
		iters += 1
	print pat_lengths	
	print "Max Pattern Index:", denoms[pat_lengths.index(max(pat_lengths))]
	print "Max Pattern Length:", max(pat_lengths)

if __name__ == '__main__':
	find_string_patterns(1000)
"""



#Here's someone else's solution that's really elegant
import itertools
def recur_len(n):
    # digits for unit fraction 1/n
    r = 10 # initial remainder (10/n)/10
    seen = {} # remainder -> first pos
    for i in itertools.count(0):
        if r == 0:
            return 0  # divides evenly.
        elif r in seen:
            return i-seen[r] # curpos - firstpos
        seen[r] = i
        r= 10*(r % n)

len,i = max((recur_len(i),i) for i in range(2,1000))
print i