import sys

print('Это не ошибка', file=sys.stdout)
print('Это ошибка', file=sys.stderr)

with open('log.txt', mode='a') as log:
	print('Привет!', file=log)