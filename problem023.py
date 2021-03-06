from eulertools import EulerProblem
from typing import List

def get_divisor_list(n:int) -> List[int]:
	divs = set()
	limit = n // 2 + 1
	for i in range(1, limit + 1):
		if n % i == 0:
			divs.add(i)
			divs.add(n // i)
	return divs

def sum_proper_divisors(n:int) -> int:
	return sum(get_divisor_list(n)) - n

def problem(args:None) -> int:
	"""Finds the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
	"""
	r = 0
	limit = 28123
	# build list of abundant numbers
	abnts = [i for i in range(1, limit) if sum_proper_divisors(i) > i]
	# create list of flags
	sum_of_abnts = [False] * limit
	# mark elements in the list that are abundant sums
	for a in range(len(abnts) + 1):
		for b in range(a):
			# use a-1 because adjusting for 0 element
			t = abnts[a - 1] + abnts[b]
			if t < limit:
				sum_of_abnts[t] = True
	# sum any element in the list that is false
	for i in range(len(sum_of_abnts)):
		if not sum_of_abnts[i]:
			r += i
	return r


# set up problem
problem_url = 'https://projecteuler.net/problem=23'
p = EulerProblem('Non-abundant sums', problem_url, None)
p.problem = problem
p.date_solved = '2021-03-05'

if __name__ == '__main__':

	# test
	p.run(n=1)

	# get average time
	p.run()