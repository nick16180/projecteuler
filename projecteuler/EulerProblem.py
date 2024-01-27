import time
import logging
from typing import Any
from dataclasses import dataclass
from tqdm import tqdm
from statistics import fmean
from pathlib import Path
from requests import get
from bs4 import BeautifulSoup as bs
from os import environ
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %I:%M:%S %p",
)


@dataclass
class EulerProblem:
    """Project Euler problem class. Provides common operations and data in one place."""

    number: int = None
    title: str = None
    url: str = None
    args: Any = None
    durations: float = None
    solution: Any = None
    durations_mean: float = None
    date_solved: str = None
    website_save_location: str = None
    website_template_location: str = None
    github_url: str = None
    header_src: str = None

    def __init__(self) -> None:
        """Initializes vars from the environment only."""
        load_dotenv()
        self.website_save_location = Path(
            environ.get("website_save_location")
        ).absolute()
        self.website_template_location = Path(
            environ.get("website_template_location")
        ).absolute()
        self.header_src = environ.get("header_src")
        return None

    def run(self, args=None, n: int = 5) -> None:
        """Run the algorithm n times and save stats.

        Args:
            args (Any, optional): Args for algorithm. Defaults to None.
            n (int, optional): Times to run algorithm. Defaults to 5.

        Returns:
            None
        """
        self.durations = []
        if self.algo is None:
            raise NotImplementedError(
                "EulerProblem algo method not implemented."
            )
        for _ in tqdm(range(n)):
            tstart = time.perf_counter()
            if args is not None:
                x = self.algo(args)
            else:
                x = self.algo(self.args)
            tend = time.perf_counter()
            self.solution = x
            self.durations.append(round(tend - tstart, 9))
        self.durations_mean = round(fmean(self.durations), 3)
        logging.info(
            f"Solution: {self.solution} in avg {self.durations_mean} seconds."
        )
        return None

    def save_for_website(self, src: Path | str) -> None:
        """Saves EulerProblem into a markdown file using a template.

        Args:
            src (Path | str): Path to source file.

        Returns:
            None
        """
        src = Path(src)
        if not src.exists():
            raise FileNotFoundError(f"{src} does not exist.")
        with open(src, "r") as io:
            pysrc = io.read()
        fn = Path(self.website_save_location) / (src.name.replace("py", "md"))
        with open(fn, "w+") as io:
            with open(self.website_template_location, "r") as io2:
                t = io2.read()
                logging.info(f"Writing to file {fn}")
                prob = bs(get(self.url).text, "html.parser")
                probtext = "".join(
                    [
                        el.get_text()
                        for el in prob.find_all(class_="problem_content")
                    ][0]
                ).strip()
                probtext_reformat = []
                for line in probtext.splitlines():
                    if len(line) < 80:
                        probtext_reformat.append(line)
                    else:
                        probtext_reformat.append(line[:80])
                        probtext_reformat.append(line[80:])
                probtext = "\n".join(probtext_reformat)
                t = (
                    t.replace("%date%", str(self.date_solved))
                    .replace("%title%", str(self.title))
                    .replace("%number%", "%03d" % self.number)
                    .replace("%source%", str(pysrc))
                    .replace("%solution%", str(self.solution))
                    .replace("%runtime%", str(self.durations_mean))
                    .replace("%problem%", probtext)
                    .replace("%github_url%", str(self.github_url))
                    .replace("%problem_url%", str(self.url))
                    .replace("%header_src%", str(self.header_src))
                )
                io.write(t)
        return None
