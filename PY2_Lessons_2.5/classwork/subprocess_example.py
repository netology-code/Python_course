import subprocess

ping_process = subprocess.run(['ping', '-t', '1', '123.55.64.12'])
print('Аргументы', ping_process.args)
print('Код возврата', ping_process.returncode)

our_process = subprocess.run(['python3', 'error_code.py'])
print('Код возврата', our_process.returncode)


python_path = '/Library/Frameworks/Python.framework/Versions/3.5/bin/python3'
our_process = subprocess.run([python_path, 'error_code.py'])
