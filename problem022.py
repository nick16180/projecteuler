from eulertools import EulerProblem
from requests import get
from typing import List

def read_data(s:str) -> List[str]:
	"""Read the list of names into a list, return it sorted.
	"""
	r = []
	d = [i for i in s.strip().split('\n') if len(i) > 0]
	for line in d:
		split_line = line.split(',')
		for line2 in split_line:
			r.append(line2.strip().replace('"', ''))
	return sorted(r)

def score(s):
	"""Compute word score as given in problem definition.
	"""
	s = s.strip().upper()
	t = 0
	for i in range(len(s)):
		t += ord(s[i]) - 64
	return t

def problem(args:str) -> int:
	"""For each word given, score it, and return the total sum of all scores.
	"""
	r = 0
	data = read_data(args)
	for i in range(len(data)):
		r += (i + 1) * score(data[i])
	return r


# set up problem
data_url = 'https://projecteuler.net/project/resources/p022_names.txt'
data = get(data_url).text

problem_url = 'https://projecteuler.net/problem=22'
p = EulerProblem('Names scores', problem_url, data)
p.problem = problem
p.date_solved = '2021-02-13'

if __name__ == '__main__':
	assert score('COLIN') == 53, 'Result incorrect'

	# test
	p.run(n=1)

	# get average time
	p.run()