import sys

print('Вывод в stdout', file = sys.stdout)
print('Вывод в stderr', file = sys.stderr)

with open('log.txt', 'w') as log:
	print('запись в лог!', file = log)