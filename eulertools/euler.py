import time
import logging
from typing import List
from progress.bar import Bar

logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s - %(levelname)s - %(message)s',
	datefmt='%Y-%m-%d %I:%M:%S %p'
)
def mean(x:List[float]) -> float:
	return(sum(x) / len(x))

class EulerProblem:
	"""Allows common operations for problems.
	"""
	def __init__(self, problem_title:str, problem_url:str, problem_args) -> None:
		self.problem_title = problem_title
		self.problem_url = problem_url
		self.problem_args = problem_args
		self.durations = None
		self.solution = None
		self.durations_mean = None
		self.date_solved = None

	def problem():
		"""The euler problem algorithm.
		"""
		pass

	def run(self, args=None, n:int=10) -> dict:
		"""Run the problem N times, save some stats.
		"""
		self.durations = []
		bar = Bar('Running', max=n)
		for i in range(n):
			tstart = time.perf_counter()
			# if args not given, use the object's arg
			if args is not None:
				x = self.problem(args)
			else:
				x = self.problem(self.problem_args)
			tend = time.perf_counter()
			self.solution = x
			self.durations.append(tend - tstart)
			bar.next()
		bar.finish()
		self.durations_mean = mean(self.durations)
		logging.info(
			'solution: %s in avg %s seconds' % 
			(self.solution, self.durations_mean)
		)
		return None

if __name__ == '__main__':
	testproblem = EulerProblem('url', 1)
	def problem(args) -> int:
		return(args + 1)
	testproblem.problem = problem
	testproblem.run(1)
	testproblem.run()