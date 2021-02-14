from eulertools import EulerProblem
from math import factorial

def problem(args:int) -> int:
	"""Sum up individual terms of a factorial-ed number N.
	"""
	s = [int(x) for x in str(factorial(args))]
	return sum(s)

# set up problem
problem_url = 'https://projecteuler.net/problem=20'
p = EulerProblem('Factorial digit sum', problem_url, 100)
p.problem = problem
p.date_solved = '2021-02-12'

if __name__ == '__main__':
	p.run(10, n=1)
	assert p.solution == 27, 'Result incorrect'

	# test
	p.run(n=1)

	# get average time
	p.run()