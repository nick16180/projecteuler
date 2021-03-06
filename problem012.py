from eulertools import EulerProblem
import numpy as np
from typing import List

def prime_list(n:int) -> List[int]:
	"""Input n>=6, Returns a array of primes, 2 <= p < n
	source: https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188
	"""
	sieve = np.ones(n//3 + (n % 6 == 2), dtype=np.bool)
	for i in range(1, int(n ** 0.5) // 3 + 1):
		if sieve[i]:
			k = 3 * i + 1 | 1
			sieve[ k * k					 // 3 :: 2 * k] = False
			sieve[ k * (k - 2 * (i & 1) + 4) // 3 :: 2 * k] = False
	return np.r_[
			2, 3, ((3 * np.nonzero(sieve)[0][1:] + 1) | 1)
	]

def problem(args:int) -> int:
	"""Generate triangle numbers until the first one reaches > N divisors.
	First solution was too slow, used algorithm in accepted answer: https://projecteuler.net/overview=012
	Triangle number = n * (n + 1) / 2, so one of these numbers n or (n + 1) / 2 must be even.
	So compute the number of divisors for n, then compute for n + 1, and so on - the process only has to be completed
	once per number, using results of last run for current.
	"""
	ndivs = 0
	tri = lambda n: int(n * (n + 1) / 2)
	primes = prime_list(10000)
	n = 3
	Dx = 2
	while ndivs <= args:
		y = n // 2 if n % 2 == 0 else n
		Dy = 1
		for p in primes:
			# stop searching because of the limit of prime divs of a number
			# multiply by 2 because this p will divide the number
			if p ** 2 > y:
				Dy = 2 * Dy
				break
			# determine number of times p can divide y, y/p, y/p/p, etc.
			# this finds power of the prime divisor
			exp = 1
			while y % p == 0:
				exp += 1
				y = y / p
			if exp > 1:
				Dy = Dy * exp
			if y == 1:
				break
		ndivs = Dx * Dy
		Dx = Dy
		n += 1
	return tri(n - 2)

# set up problem
problem_url = 'https://projecteuler.net/problem=12'
p = EulerProblem('Highly divisible triangular number', problem_url, 500)
p.problem = problem
p.date_solved = '2021-02-09'

if __name__ == '__main__':
	p.run(5, n=1)
	assert p.solution == 28, 'Result incorrect'

	# test
	p.run(n=1)

	# get average time
	p.run()