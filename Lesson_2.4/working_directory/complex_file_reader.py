import os

with open('myfile.txt') as f:
	print(f.read())

os.chdir('another_directory')

with open('myfile.txt') as f:
	print(f.read())