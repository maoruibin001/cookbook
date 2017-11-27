# Determine if any .py files exist in a directory
import os

files = os.listdir()

n = [name for name in files if name.endswith('.git')]
print(sum([1, 2,3]))
print(any(name.endswith('.git') for name in files))
