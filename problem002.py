from eulertools import EulerProblem
import numpy as np

def problem(args:int) -> int:
	"""Create a fibonacci sequence up to a given limit. Take the sum of any even terms.
	"""
	a, b, c =  1, 2, 0
	result = [a]
	while c <= args:
		c = a + b
		a = b
		b = c
		result.append(a)
	result = np.array(result)
	return sum(result[result % 2 == 0])

# set up problem
problem_url = 'https://projecteuler.net/problem=2'
p = EulerProblem('Even Fibonacci numbers', problem_url, 4000000 - 1)
p.problem = problem
p.date_solved = '2021-01-29'

if __name__ == '__main__':
	# test the given input
	p.run(89, n=1)
	check = np.array([1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
	assert p.solution == sum(check[check % 2 == 0]), 'Result incorrect'

	# test
	p.run(n=1)

	# get average time
	p.run()