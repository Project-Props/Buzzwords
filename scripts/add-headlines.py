import glob
import re

"""
This script will run through all files who's
name starts with a digit and are empty. It will then
add headline to each of those
"""

def starts_with_digit(string):
    return bool(re.search("^\d+", string))

def read_file(path):
    return open(path, 'r').read()

def file_empty(file):
    return read_file(file) == ''

def digit_in_filename(filename):
    return re.search("^(\d+).*", file).group(1)

def files_starting_with_a_digit():
    return filter(starts_with_digit, glob.glob("*"))

def headline_for_file(file):
    headline = "Buzzwords from chapter {0}\n".format(digit_in_filename(file))
    return headline + ("=" * (len(headline) - 1))

for file in files_starting_with_a_digit():
    if file_empty(file):
        open(file, 'w').write(headline_for_file(file))

