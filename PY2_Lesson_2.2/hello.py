def print_hello():
	f = open('hello.txt')
	for line in f:
		print(line.strip())
	f.close()

def print_hello2():
	with open('hello.txt') as f:
		for line in f:
			print(line.strip())

print_hello2()