"emulate directory navigation and add up directory sizes"

from itertools import accumulate
from collections import defaultdict

# counter
directory_sizes = defaultdict(int)

# open file
for line in open(r"C:\Users\micah\PycharmProjects\python-practice-and-challenges\advent_of_code\advent_day_7\day_7.txt"):
    # split line by command inputs
    match line.split():
        # return to root directory
        case "$", "cd", "/":
            current_directory = ["/"]

        # do nothing
        case "$", "ls":
            pass

        # remove the last directory to move out one
        case "$", "cd", "..":
            current_directory.pop()

        # move to the given directory by adding to list
        case "$", "cd", directory:
            current_directory.append(directory + "/")

        # do nothing
        case "dir", directory:
            pass

        # if it has a size and filename, add size to the size dictionary with given directory as the key
        case size, file_name:
            for directory in accumulate(current_directory):
                directory_sizes[directory] += int(size)

# print total of all that are less than 100_000
print(sum([value for value in directory_sizes.values() if value <= 100000]))

# print smallest directory that, if deleted, would free up enough space
total_space = 70_000_000
unused_space = 30_000_000
print(min(value for value in directory_sizes.values() if value >= (unused_space - (total_space - directory_sizes["/"]))))

