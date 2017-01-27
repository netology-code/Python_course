import os

path1 = "another_directory/data/dictionary.txt"
path2 = "another_directory\\data\\dictionary.txt"

constructed_path = os.path.join("another_directory", "data", "dictionary.txt")
print(constructed_path)