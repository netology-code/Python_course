import sys
import os

print(sys.argv)
print(os.environ['PATH'])
print("error", file=sys.stderr)

exit(15)