from eulertools import EulerProblem
from typing import Tuple, List
from math import factorial

def problem(args:Tuple[int, List[str]]) -> str:
	"""Finds Nth lexicographic permutation of given digits.
	"""
	r = ''
	limit = args[0]
	remaining = [i for i in range(args[1] + 1)]
	# current position in ordered list
	position = 1
	while len(remaining) > 1:
		# running sum for checking if we have gone over the target element
		s = position
		# index of element
		c = 0
		# number of possible unique combinations after fixing the first element
		p = factorial(len(remaining) - 1)
		# count the number of possible combinations
		# stop when we have gone over the target
		while s <= limit and c < 10:
			s += p
			c += 1
		# since s and c have been incremented, need to decrement for
		# the actual answer
		r += str(remaining[c - 1])
		remaining.pop(c - 1)
		position = s - p
	r += str(remaining[0])
	return r

# set up problem
problem_url = 'https://projecteuler.net/problem=24'
p = EulerProblem('Lexicographic permutations', problem_url, (1000000, 9))
p.problem = problem
p.date_solved = '2021-03-05'

if __name__ == '__main__':
	p.run((6, 2), n=1)
	assert p.solution == '210', 'Result incorrect'

	# test
	p.run(n=1)

	# get average time
	p.run()