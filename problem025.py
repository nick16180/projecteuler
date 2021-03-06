from eulertools import EulerProblem
from math import log

# fibonacci sequence formula for n digit number
f = lambda n: (n * log(10) + log(5 ** .5)) / log((1 + 5 ** .5) / float(2))

def problem(args:int) -> int:
	"""Finds N-digit Fibonacci number.
	Derived on paper, see here for a similar one: https://blog.dreamshire.com/solutions/project_euler/project-euler-problem-025-solution/
	"""
	return int(f(args - 1)) + 1

# set up problem
problem_url = 'https://projecteuler.net/problem=25'
p = EulerProblem('1000-digit Fibonacci number', problem_url, 1000)
p.problem = problem
p.date_solved = '2021-03-06'

if __name__ == '__main__':
	p.run(3, n=1)
	assert p.solution == 12, 'Result incorrect'

	# test
	p.run(n=1)

	# get average time
	p.run()