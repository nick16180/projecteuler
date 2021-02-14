from eulertools import EulerProblem
import numpy as np
from typing import List

def read_data(s:str) -> List[List[int]]:
	"""Read the table of strings to a table of ints.
	"""
	d = s.strip().split('\n')
	return [[int(j) for j in i.strip().split(' ')] for i in d]

def problem(args:List[List[int]]) -> int:
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
data = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

problem_url = 'https://projecteuler.net/problem=18'
p = EulerProblem('Maximum path sum I', problem_url, data)
p.problem = problem
p.date_solved = '2021-02-12'

if __name__ == '__main__':
	# test
	p.run(n=1)

	# get average time
	p.run()