#!/usr/bin/env python3
"""Regex Search

Practice Project

A program that opens all .txt files in a folder
and searches for any line that matches a user-supplied
regular expression. The matching lines are printed to the screen.
"""
import re
import sys
from pathlib import Path

# User-supplied regex for the search.
print("Enter your regex pattern:")
userRegex = r'' + input()
try:
    re.search(userRegex, '')
except re.error as e:
    print(e.msg)
    sys.exit()

# All .txt in current folder.
allTxt = list(Path.cwd().glob('*.txt'))
for file in allTxt:
    with open(file) as f:
        for line in list(f):
            if re.findall(userRegex, line):
                # Print lines that match the regex.
                print(line, end='')
