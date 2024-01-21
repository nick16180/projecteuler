from projecteuler.tools import EulerProblem
import numpy as np


def problem(args: int) -> int:
    """Sum of number divisible by 3 and 5. Numbers divisible by both are counted in both, so remove the sum of them.."""
    n = np.arange(args)
    n = np.add(1, n)
    x = n[n % 3 == 0]
    y = n[n % 5 == 0]
    z = n[n % (5 * 3) == 0]
    return sum(x) + sum(y) - sum(z)


# # set up problem
# problem_url = "https://projecteuler.net/problem=1"
# p = EulerProblem("Multiples of 3 and 5", problem_url, 1000 - 1)
# p.problem = problem
# p.date_solved = "2021-01-29"

# if __name__ == "__main__":
#     # test the given input
#     p.run(10 - 1, n=1)
#     assert p.solution == 23, "Result incorrect"

#     # test
#     p.run(n=1)

#     # get average time
#     p.run()
