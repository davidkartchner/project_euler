"""
David Kartchner
Project Euler Max Triangle Path Sum (Problems 18, 67)
May 12, 2016
"""

def max_path_sum(filename):
	f = open(filename, 'r')
	tri_rows = []

	for line in f:
		tri_rows.append([int(i) for i in line.split()])


	prev_row = [0]
	curr_row=[]
	for i in xrange(len(tri_rows)):
		curr_row = tri_rows[i]
		curr_row[0]+=prev_row[0]
		curr_row[-1]+=prev_row[-1]
		for j in xrange(1, len(tri_rows[i])-1):
			curr_row[j]+=max([prev_row[j-1], prev_row[j]])
		prev_row = curr_row[:]
	return max(curr_row)
print max_path_sum('p67_triangle.txt')