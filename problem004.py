from eulertools import EulerProblem

def is_palindrome(n:int) -> bool:
	"""Check if given integer is a palindrome (same read forward as backwards).
	"""
	s = str(n)
	pal = True
	i = int(len(s)/2)
	while pal and i > 0:
		pal = ord(s[i-1]) == ord(s[-i])
		i -= 1
	return pal

def problem(args:None) -> int:
	"""Find largest palindrome P that is a product of 3-digit numbers.
	So:
	- P must be between 100,000 and 1,000,000.
	- P = X * Y, X and Y are 3-digit numbers.
	- P = 100000a + 10000b + 1000c + 100c + 10b + a.
	- P = 100001a + 10010b + 1100c.
	- P = 11(9091a + 910b + 100c), so P is divisible by 11.
	- Max of values to search through: 999 * 999.
	- Min of values to search through: 902 * 902.
	 - 902 is the smallest integer > 900 divisible by 11. Since the largest palindrome contains at least 1 number divisible by 11, this lower bound makes sense. 
	"""

	x = 999
	y = 990 # largest value < 1000 divisible by 11
	# search for palindrome
	while not is_palindrome(x*y) and x != 902:
		y -= 1 # decrement y until it reaches 902
		# if y gets to 902, reset y then decrement x
		if y == 902:
			y = 990
			x -= 1
	return x * y

# set up problem
problem_url = 'https://projecteuler.net/problem=4'
p = EulerProblem('Largest palindrome product', problem_url, None)
p.problem = problem
p.date_solved = '2021-01-29'

if __name__ == '__main__':
	assert is_palindrome(250052), '1. Result incorrect'
	assert not is_palindrome(15), '2. Result incorrect'

	# test
	p.run(n=1)

	# get average time
	p.run()