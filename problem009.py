from eulertools import EulerProblem

def problem(args:int) -> int:
	"""Find pythagorean triple a, b, c where a + b + c = N
	"""
	for b in range(1, args):
		for a in range(1, b + 1):
			c = args - a - b
			if a**2 + b**2 == c**2 and a < b < c:
				return a * b * c

# set up problem
problem_url = 'https://projecteuler.net/problem=9'
p = EulerProblem('Special Pythagorean triplet', problem_url, 1000)
p.problem = problem
p.date_solved = '2021-01-29'

if __name__ == '__main__':
	# test
	p.run(n=1)

	# get average time
	p.run()