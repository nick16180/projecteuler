from eulertools import EulerProblem

def problem(args:int) -> int:
	"""Sum of digits of 2 ^ N.
	"""
	s = 0
	for i in str(2 ** args):
		s += int(i)
	return s

# set up problem
problem_url = 'https://projecteuler.net/problem=16'
p = EulerProblem('Power digit sum', problem_url, 1000)
p.problem = problem
p.date_solved = '2021-02-10'

if __name__ == '__main__':
	# test
	p.run(n=1)

	# get average time
	p.run()