from eulertools import EulerProblem
from requests import get
from typing import List

def read_data(s:str) -> List[List[int]]:
	"""Read the table of strings to a table of ints.
	"""
	d = s.strip().split('\n')
	return [[int(j) for j in i.strip().split(' ')] for i in d]

def problem(args:str) -> int:
	"""Find largest sum of all paths from top to bottom.
	"""
	dt = read_data(args)
	for i in range(len(dt) - 1):
		largest = 0
		for j in range(len(dt[i])):
			x = dt[i][j] # current
			y = dt[i + 1][j] # value below
			z = dt[i + 1][j + 1] # value below + right
			# if on left edge, add current/below only
			if j == 0:
				dt[i + 1][j] = x + y
				largest = x + z
			# if on right edge, add current/below + right
			if j == len(dt[i]) - 1:
				dt[i + 1][j + 1] = x + z
			# if not on edges
			if 0 < j < len(dt[i]):
				if largest < (x + y):
					dt[i + 1][j] = x + y
				else:
					dt[i + 1][j] = largest
				largest = x + z
	return max(dt[len(dt) - 1])

# set up problem
data_url = 'https://projecteuler.net/project/resources/p067_triangle.txt'
data = get(data_url).text

problem_url = 'https://projecteuler.net/problem=67'
p = EulerProblem('Maximum path sum II', problem_url, data)
p.problem = problem
p.date_solved = '2021-02-12'

if __name__ == '__main__':
	# test
	p.run(n=1)

	# get average time
	p.run()