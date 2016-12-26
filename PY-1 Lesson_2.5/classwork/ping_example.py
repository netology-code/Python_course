import subprocess

print('---------')
e = subprocess.run(['ping', '-s', '200', '-c', '2', 'google.com'])
print('#########')
print(type(e))
print(e)
print('Код возврата: ', e.returncode)