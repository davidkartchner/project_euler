"""
David Kartchner
Project Euler Problem 22
May 13, 2016
"""
import re

f = open("p22_names.txt", 'r')
file_contents = list(f.read().split(','))
names = [re.sub('"', '', line) for line in file_contents]

	
names = sorted(names)


def name_value(name):
	numberfied_name = [ord(char) -64 for char in name]
	return sum(numberfied_name)

name_sum = 0
for i in xrange(len(names)):
	name_sum+= (i+1)*name_value(names[i])
print name_sum
