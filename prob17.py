"""
David Kartchner
Project Euler Problem 17
May 11, 2016
"""

a = {'one':3, 'two':3, 'three':5, 'four':4, 'five':4, 'six':3, 'seven':5, 'eight':5, 'nine':4, 'ten':3, 'eleven':6, 'twelve':6, 'thirteen':8, 'fourteen':8, 'fifteen':7, 'sixteen':7, 'seventeen':9, 'eighteen':8, 'nineteen':8, 'twenty':6, 'thirty':6, 'forty':5, 'fifty':5, 'sixty':5, 'seventy':7, 'eighty':6, 'ninety':6, 'hundred':7, 'thousand':8, 'and':3}

letter_sum = 191*a['one'] + a['thousand'] + 190*(a['two'] + a['three'] + a['four'] + a['five'] + a['six'] + a['seven'] + a['eight'] + a['nine']) + 900*a['hundred'] + 9*99*a['and'] + 100*(a['twenty'] + a['thirty'] + a['forty'] + a['fifty'] + a['sixty'] + a['seventy'] + a['eighty'] + a['ninety']) + 10*(a['ten'] + a['eleven'] + a['twelve'] + a['thirteen'] + a['fourteen'] + a['fifteen'] + a['sixteen'] + a['seventeen'] + a['eighteen'] + a['nineteen'])

print letter_sum