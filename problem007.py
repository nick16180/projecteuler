from eulertools import EulerProblem
import numpy as np
from typing import List
from math import log

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
	"""Find the nth prime. Simplified by using bounds on the limit needed to find that prime.
	source: https://en.wikipedia.org/wiki/Prime_number_theorem
	"""
	limit = int(args * log(args) + args * log( log(args) ) + 1)
	primes = prime_list(limit)
	if len(primes) >= args:
		return primes[args-1]
	else:
		return -1

# set up problem
problem_url = 'https://projecteuler.net/problem=7'
p = EulerProblem('10001st prime', problem_url, 10001)
p.problem = problem
p.date_solved = '2021-01-29'

if __name__ == '__main__':
	p.run(6, n=1)
	assert p.solution == 13, 'Result incorrect'

	# test
	p.run(n=1)

	# get average time
	p.run()