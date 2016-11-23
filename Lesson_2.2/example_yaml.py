# pip install pyyaml
import yaml
from pprint import pprint

with open('godFather.yml') as godfather_file:
	movie = yaml.load(godfather_file, Loader=yaml.Loader)
	pprint(movie)
