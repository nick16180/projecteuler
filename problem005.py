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

def prime_divisors(x:int) -> List[dict]:
	"""Get list of prime divisors of a number and the degree of the prime divisor.
	"""
	divs = []
	if x == 0 or x == 1:
		return None
	primes = prime_list(int(x // 2 + 1))
	for p in primes:
		toadd = {} # item to add to the list
		# add a divisor when found, the initial degree is 1
		if x % p == 0:
			n = 2
			toadd = {'prime': p, 'degree': n-1}
			# keep checking until the division isn't even
			while x % (p ** n) == 0:
				n += 1
				toadd = {'prime': p, 'degree': n-1}
		if len(toadd) > 0:
			divs.append(toadd)
	return divs

def problem(args:int) -> int:
	"""Find smallest number that is divisible by each number from 1 to limit.
	This means that the number is divisible by each prime up to limit and all other composite numbers.
	"""
	primes = np.array(prime_list(args))
	nonprimes = np.setdiff1d(np.arange(1, args + 1), primes)
	# find divisors of each of the nonprimes
	t = [prime_divisors(i) for i in nonprimes]
	# remove items that are None
	t = [i for i in t if i is not None]
	# want to figure out the highest power of the composites for each given
	nonprimes_divs1 = []
	# get divisors for each number
	for item in t:
		for i in range(len(item)):
			nonprimes_divs1.append(item[i])
	# sort the divisors for each number so that the number with the highest degree is first for each number
	nonprimes_divs2 = sorted(
		nonprimes_divs1,
		key=lambda x: (x.get('prime'), x.get('degree')),
		reverse=True
	)
	# figure out which primes to keep
	# instead of the prime^degree, save it as the prime repeated degree times
	nonprimes_divs3 = []
	primes_used = []
	for i in nonprimes_divs2:
		if i.get('prime') not in primes_used:
			primes_used.append(i.get('prime'))
			nonprimes_divs3 = nonprimes_divs3 + ([i.get('prime')] * i.get('degree'))
	# find the product of this list, then divide by the values in primes that also appear in that list
	nonprimes_divs_product = np.product(np.array(nonprimes_divs3))
	for p in primes:
		if p in nonprimes_divs3:
			nonprimes_divs_product = nonprimes_divs_product / p
	return int(np.prod(primes) * nonprimes_divs_product)

# set up problem
problem_url = 'https://projecteuler.net/problem=5'
p = EulerProblem('Smallest multiple', problem_url, 20)
p.problem = problem
p.date_solved = '2021-01-29'

if __name__ == '__main__':
	p.run(10)
	assert p.solution == 2520, 'Result incorrect'

	# test
	p.run(n=1)

	# get average time
	p.run()