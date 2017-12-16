"""
David Kartchner
Project Euler Problem 16
May 11, 2016
"""

big_string = str(2**1000)
digit_list = [int(i) for i in big_string]
digit_sum = sum(digit_list)
print digit_sum