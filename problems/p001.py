from projecteuler.EulerProblem import EulerProblem
from dotenv import load_dotenv
from os import environ
from pathlib import Path
import numpy as np


def algo(args: int) -> int:
    """Sum of numbers divisible by 3 and 5. Numbers divisible by both are
    counted in both, so remove the sum of them."""
    n = np.arange(args)
    n = np.add(1, n)
    x = n[n % 3 == 0]
    y = n[n % 5 == 0]
    z = n[n % (5 * 3) == 0]
    return sum(x) + sum(y) - sum(z)


# set up problem
load_dotenv()
p = EulerProblem()
p.number = 1
p.title = "Multiples of 3 and 5"
p.args = 1000 - 1
p.url = f"https://projecteuler.net/problem={p.number}"
p.algo = algo
p.date_solved = "2024-01-21"
p.github_url = environ.get("github_url") + "/".join(
    ["problems", Path(__file__).name]
)

if __name__ == "__main__":
    # test the given input
    p.run(10 - 1, n=1)
    assert p.solution == 23, "Result incorrect"

    # test
    p.run(n=1)

    # get average time
    p.run()

    # save to website markdown
    p.save_for_website(__file__)
