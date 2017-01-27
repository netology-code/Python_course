import os
print('Это англо-русский переводчик!')

print(__file__)
print(os.path.realpath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))

base_path = os.path.dirname(os.path.realpath(__file__))
dictionary_path = os.path.join(base_path, 'dictionary.txt')

print(dictionary_path)
with open(dictionary_path) as d:
	print(d.read())

os.chdir(base_path)
with open('dictionary.txt') as d:
	print(d.read())