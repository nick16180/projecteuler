from eulertools import EulerProblem
import numpy as np
from typing import List

def gcd(a:int, b:int) -> int:
	"""Computes between greatest common divisor 2 numbers.
	source: https://en.wikipedia.org/wiki/Euclidean_algorithm
	"""
	if a == 0:
		return b
	else:
		return gcd(b % a, a)

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

def problem(args:None) -> int:
	"""Finds the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
	"""
	r = 0
	primes = prime_list(1000)
	order = 0
	for p in primes:
		for i in range(1, p):
			if gcd(p, 10) == 1:
				if (10 ** i) % p == 1:
					order = max(order, i)
					r = p if order == i else r
					break
	return r

# set up problem
problem_url = 'https://projecteuler.net/problem=26'
p = EulerProblem('Reciprocal cycles', problem_url, None)
p.problem = problem
p.date_solved = '2021-03-06'

if __name__ == '__main__':

	# test
	p.run(n=1)

	# get average time
	p.run()