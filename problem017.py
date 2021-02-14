from eulertools import EulerProblem

def letter_count(x:int) -> int:
		letter_counts = {
			1:3, 2:3, 3:5, 4:4, 5:4,
			6:3, 7:5, 8:5, 9:4, 10:3,
			11:6, 12:6, 13:8, 14:8, 15:7,
			16:7, 17:9, 18:8, 19:8, 20:6,
			30:6, 40:5, 50:5, 60:5, 70:7,
			80:6, 90:6, 100: 7
		}
		# take care of extreme cases
		if x == 0:
			return 4
		if x == 1000:
			return letter_counts[1] + 8
		# letter sum
		n = 0
		# look at numbers below 100
		y = x % 100
		if 1 <= y <= 20: 
			n += letter_counts[y]
		elif y > 20:
			n += letter_counts[y % 10] if y % 10 != 0 else 0
			n += letter_counts[y - y % 10]
		# take care of "and"
		if x > 100 and y != 0:
			n += 3
		# look at numbers above 100, only consider 100s place
		y = (x % 1000 - x % 100)/100
		if 1 <= y <= 9:
			n += letter_counts[y] + letter_counts[100]
		return n

def problem(args:int) -> int:
	"""Count number of letters when numbers are written out up to N.
	This only works up to N = 1000.
	"""
	s = 0
	for i in range(1, args + 1):
		s += letter_count(i)
	return s

# set up problem
problem_url = 'https://projecteuler.net/problem=17'
p = EulerProblem('Number letter counts', problem_url, 1000)
p.problem = problem
p.date_solved = '2021-02-11'

if __name__ == '__main__':
	p.run(5, n=1)
	assert p.solution == 19, 'Result incorrect'

	# test
	p.run(n=1)

	# get average time
	p.run()