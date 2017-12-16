"""
David Kartchner
Project Euler Problem 19
May 12, 2016
"""
def calc_start_day(year):
	pass


def count_sundays_on_first(startyear, endyear):
	sundays=0
	day=1
	month_mods = [3,0,3,2,3,2,3,3,2,3,2,3]
	leap_month_mods = [3,1,3,2,3,2,3,3,2,3,2,3]
	for year in xrange(startyear, endyear+1):	
		leap=False
		if year%4==0:
			if year%100==0:
				if year%400==0:
					leap=True
			else:
				leap=True
		if leap==True:
			for i in leap_month_mods:
				if day%7==1:
					sundays += 1
				day += i
		else:
			for i in month_mods:
				if day%7==1:
					sundays += 1
				day += i
	return sundays

print count_sundays_on_first(1901, 2000)

		