from eulertools import EulerProblem

def problem(args:int) -> int:
	"""Find number < N which produces longest collatz chain.
	"""
	maxlen = 0
	r = None
	lens = {}
	i = 1
	while i < args:
		j = i # start of collatz chain
		c = 1 # keep track of length
		while j != 1:
			if j in lens:
				# subtract 1 since current value is j
				# when j was calculated before, it included itself
				# as part of the chain length
				c += lens[j] - 1
				break
			c += 1
			j = j // 2 if j % 2 == 0 else 3 * j + 1
		maxlen = max(c, maxlen)
		r = i if maxlen == c else r
		# save the chain lengths
		if i not in lens:
			lens[i] = c
		i += 1
	return r

# set up problem
problem_url = 'https://projecteuler.net/problem=14'
p = EulerProblem('Longest Collatz sequence', problem_url, 1000000)
p.problem = problem
p.date_solved = '2021-02-10'

if __name__ == '__main__':
	# test
	p.run(n=1)

	# get average time
	p.run()