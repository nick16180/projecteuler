from eulertools import EulerProblem
import numpy as np

def problem(args:int) -> int:
	"""Find A - B where
	A = (sum of i for natural numbers i to limit) ^ 2
	B = (sum of i^2 for natural numbers i to limit)
	"""
	A = (args * (args + 1) / 2) ** 2
	B = np.dot(np.arange(1, args + 1), np.arange(1, args + 1))
	return int(A - B)

# set up problem
problem_url = 'https://projecteuler.net/problem=6'
p = EulerProblem('Sum square difference', problem_url, 100)
p.problem = problem
p.date_solved = '2021-01-29'

if __name__ == '__main__':
	p.run(10, n=1)
	assert p.solution == 2640, 'Result incorrect'

	# test
	p.run(n=1)

	# get average time
	p.run()