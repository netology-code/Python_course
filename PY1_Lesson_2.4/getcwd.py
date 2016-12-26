import os

print('Before:', os.getcwd())
os.chdir('games')
print('After:', os.getcwd())