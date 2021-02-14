from eulertools import EulerProblem

def problem(args:int) -> int:
	"""Compute number of ways to make N where
	N = a + 2b + 5c + 10d + 20e + 50f + 100g + 200h
	"""
	r = 0
	target = args
	for h in range(target // 200 + 1):
		s1 = target - h * 200
		for g in range(s1 // 100 + 1):
			s2 = s1 - g * 100
			for f in range(s2 // 50 + 1):
				s3 = s2 - f * 50
				for e in range(s3 // 20 + 1):
					s4 = s3 - e * 20
					for d in range(s4 // 10 + 1):
						s5 = s4 - d * 10
						for c in range(s5 // 5 + 1):
							s6 = s5 - c * 5
							for b in range(s6 // 2 + 1):
								s7 = s6 - b * 2
								for a in range(s7 + 1):
									s8 = s7 - a
									if s8 == 0:
										r += 1
	return r


# set up problem
problem_url = 'https://projecteuler.net/problem=31'
p = EulerProblem('Coin sums', problem_url, 200)
p.problem = problem
p.date_solved = '2021-02-14'

if __name__ == '__main__':

	# test
	p.run(n=1)

	# get average time
	p.run()