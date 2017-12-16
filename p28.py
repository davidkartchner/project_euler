"""
David Kartchner
Project Euler Problem 28--Diagonal Spiral
May 21, 2016
"""

def diagonal_spiral_sum(n):
    diag_sum = 1
    current_num = 1
    for i in xrange(2,n,2):
        for j in xrange(4):
            current_num += i
            diag_sum += current_num
        print i
    print diag_sum

if __name__ == '__main__':
    diagonal_spiral_sum(1001)
