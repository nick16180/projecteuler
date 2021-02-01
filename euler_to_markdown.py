from pathlib import Path
import importlib
import os
from shutil import copyfile
import logging
from typing import List, Tuple

COPY_TO_FOLDER = True
DEST_FOLDER = 'D:/share/workspace/website/root/site/content/posts/projecteuler'

logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s - %(levelname)s - %(message)s',
	datefmt='%Y-%m-%d %I:%M:%S %p'
)

def to_md_table(data:List[Tuple], head:List[str]) -> str:
	"""Convert an array of numbers to a markdown table
	"""
	s = ['| ' + ' | '.join(head) + ' |']
	s += ['| --- | --- |']
	s += ['| ' + ' | '.join([str(i[0]), '{:.4f}'.format(i[1])]) + ' |' for i in data]
	return '\n'.join(s)

# get path of the folder where this file lives
thispath = Path(os.path.dirname(os.path.realpath(__file__)))

# get markdown markdown file and folder
markdown_template_file = thispath / 'euler_md_template.md'
markdown_folder = thispath / 'to_markdown'

markdown_template = None
with open(markdown_template_file) as io:
	markdown_template = io.read()

# for each file, import it, run the problem, then create some output
problem_results = []
for file in list(thispath.glob('problem*.py')):
	# import the file into the namespace and run methods from the object
	logging.info('importing and running file: %s' % (file.as_posix()))
	this_module_name = file.stem
	this_module = importlib.import_module(this_module_name)
	try:
		# load and run the problem
		this_problem = this_module.p
		this_problem.run()
		# read the file
		source = None
		with open(file) as io:
			source = io.read()
		# create a list of durations to make into a table
		x = this_problem.durations + [this_problem.durations_mean]
		i = [str(i+1) for i in range(len(x)-1)] + ['Mean']
		ix = zip(i,x)
		# update the markdown text
		md_data = markdown_template\
			.replace('%number%', 	this_module_name.replace('problem', '').replace('.py', ''))\
			.replace('%date%', 		this_problem.date_solved)\
			.replace('%source%', 	'```python\n' + source + '\n```')\
			.replace('%url%', 		this_problem.problem_url)\
			.replace('%desc%', 		this_problem.problem_title)\
			.replace('%durations%', '\n' + to_md_table([i for i in ix], ['Run #', 'Duration (s)']) + '\n')
		# save the markdown text to a file
		outfile = str(markdown_folder / this_module_name) + '.md'
		with open(outfile, 'w+') as io:
			io.writelines(md_data)
		# copy to the folder if necessary
		if COPY_TO_FOLDER:
			copyfile(outfile, str(Path(DEST_FOLDER) / this_module_name) + '.md')
	except Exception as e:
		logging.exception(e)
		pass