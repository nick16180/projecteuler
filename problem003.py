from eulertools import EulerProblem

def is_prime(n: int) -> bool:
	"""Primality test using 6k+-1 optimization.
		source: https://en.wikipedia.org/wiki/Primality_test
	"""
	if n <= 3:
		return n > 1
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i ** 2 <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True

def problem(args:int) -> int:
	"""Starting at sqrt of n (the highest limit to search for divisors), search for largest prime that divides n.
	"""
	limit = int(args ** .5)
	for i in reversed(range(limit)):
		if args % i == 0:
			if is_prime(i):
				return i

# set up problem
problem_url = 'https://projecteuler.net/problem=3'
p = EulerProblem('Largest prime factor', problem_url, 600851475143)
p.problem = problem
p.date_solved = '2021-01-29'

if __name__ == '__main__':
	# test the given input
	p.run(13195, n=1)
	assert p.solution == 29, 'Result incorrect'

	# test
	p.run(n=1)

	# get average time
	p.run()