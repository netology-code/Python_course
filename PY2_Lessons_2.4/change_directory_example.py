import os

print('Текущая директория: ', os.getcwd())
with open('data.txt') as data:
	print(data.read())
with open('another_directory/data.txt') as data:
	print(data.read())

os.chdir('another_directory')
print('Текущая директория: ', os.getcwd())
with open('data.txt') as data:
	print(data.read())