import os
import os.path

with open('myfile.txt') as f:
	print(f.read())

with open(os.path.join('another_directory', 'myfile.txt')) as f:
	print(f.read())