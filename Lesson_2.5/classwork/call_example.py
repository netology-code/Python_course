import subprocess

print('---------')
e = subprocess.run(['python3', 'process_example.py'])
print('#########')
print(type(e))
print(e)
print('Программа напечатала:')
print(e.stdout)
print('Код возврата: ', e.returncode)