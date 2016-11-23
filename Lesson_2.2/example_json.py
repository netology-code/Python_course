import json
from pprint import pprint

# with open('godFather.json') as godfather_file:
# 	movie = json.load(godfather_file)
# 	pprint(movie)


coutries = [
	{"name": "Russia"},
	{"name": "USA"},
]
with open('coutries_example.json', 'w') as example_file:
	json.dump(coutries, example_file)