


def is_palindrome(num):
	if str(num)==str(num)[::-1]:
		return True
	else:
		return False

#Find largest palindrome that is product of two "digits"-digit numbers
def find_largest_palindrome(digits):
	floor = 8*10**(digits-1)
	palindromes = []
	nines=['9']*digits
	i=int(''.join(nines))
	j=i
	a=i
	k=0
	num = floor
	while i>floor:
		while j>floor:
			n = i*j
			if n > num:
				if is_palindrome(n):
					palindromes.append(n)
					num=n
			j-=1
		i-=1	
		k+=1

		j=a-k

	return palindromes

if __name__=="__main__":
	print find_largest_palindrome(3)

