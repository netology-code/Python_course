# пример ловли исключения, при делении на ноль
def division():
	try: 
		a = 3/0
		print(a)
	except:
		print('ай яй яй. на ноль делить нельзя')

# пример чтения из файла, и если такого файла нет, то создание его
def read_or_create1():
	filename = 'this_file_not_exists'
	try:
		with open(filename) as f:
			return f.read()
	except FileNotFoundError:
		with open(filename, 'w') as f:
			pass

# пример чтения из файла, и если такого файла нет, то создание его
# при помощи os.path
import os.path
def read_or_create2():
	filename = 'this_file_not_exists'
	if os.path.isfile(filename):
		with open(filename) as f:
			return f.read()
	else:
		with open(filename, 'w') as f:
			pass
read_or_create2()