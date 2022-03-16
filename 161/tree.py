import os


def count_dirs_and_files(directory="."):
    """Count the amount of of directories and files in passed in "directory" arg.
    Return a tuple of (number_of_directories, number_of_files)
    """
    count_dirs = 0
    count_files = 0
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            count_dirs += 1
        for file in files:
            count_files += 1
    return count_dirs, count_files
