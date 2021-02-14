from eulertools import EulerProblem
from typing import List

def get_divisor_list(n:int) -> List[int]:
	"""Get a list of divisors of a number.
	"""
	divs = set()
	limit = int(n / 2) + 1
	for i in range(1, limit + 1):
		if n % i == 0:
			divs.add(i)
			divs.add(n // i)
	return divs

def get_divisor_sum(n:int) -> int:
	"""Compute sum of divisors of a number, less itself.
	"""
	divs = get_divisor_list(n)
	divs.remove(n)
	return sum(divs)

def problem(args:int) -> int:
	"""Find sum of amicable numbers up to N.
	"""
	div_list = {}
	r = 0
	# get the divisor sums of values of 1 to N
	for i in range(1, args + 1):
		t = get_divisor_sum(i)
		if 1 < t <= 10000:
			div_list[i] = t
	# for each key (K) in div_list, look for its value (V) in div_list (as a key J)
	# if found, check that J's value W is K and that K != V
	# in symbols, check that dict[J] (= W) == K and dict[K] (= V) == J
	for i in div_list:
		if div_list[i] in div_list:
			if div_list[div_list[i]] == i and div_list[i] != i:
				r += i
	return r

# set up problem
problem_url = 'https://projecteuler.net/problem=21'
p = EulerProblem('Amicable numbers', problem_url, 10000)
p.problem = problem
p.date_solved = '2021-02-13'

if __name__ == '__main__':

	# test
	p.run(n=1)

	# get average time
	p.run()