from eulertools import EulerProblem
from scipy.special import comb

def problem(args:int) -> int:
	"""Find number of paths on a grid N x N from top left to bottom right.
	Can only move down or right.
	Solution uses nCr (n Choose r) because the total path length is always N x 2
	and there are always N moves down and N moves right.
	So, nCr finds number of ways r objects can be chosen from n total.
	"""
	return comb(args * 2, args, exact=True)

# set up problem
problem_url = 'https://projecteuler.net/problem=15'
p = EulerProblem('Lattice paths', problem_url, 20)
p.problem = problem
p.date_solved = '2021-02-10'

if __name__ == '__main__':
	# test
	p.run(n=1)

	# get average time
	p.run()