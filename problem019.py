from eulertools import EulerProblem

def lands_on_weekday(n):
	days = [i for i in range(6 + 1)]
	return days[n % 7]

def problem(args:None) -> int:
	"""Count number of Sundays that occur on first month each year
	during the 20th century.
	"""
	month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
	month_days_leap = [31,29,31,30,31,30,31,31,30,31,30,31]
	year = 1901
	day = 366
	r = 0
	for y in range(100):
		adjusted_days = month_days
		if (y + year) % 4 == 0 and (y + year) % 400 != 0:
			adjusted_days = month_days_leap
		if (y + year) % 400 == 0:
			adjusted_days = month_days_leap
		for m in adjusted_days:
			r += 1 if lands_on_weekday(day) == 0 else 0
			day += m
	return r

# set up problem
problem_url = 'https://projecteuler.net/problem=19'
p = EulerProblem('Counting Sundays', problem_url, None)
p.problem = problem
p.date_solved = '2021-02-12'

if __name__ == '__main__':
	# test
	p.run(n=1)

	# get average time
	p.run()