#!/usr/bin/env python3
# Date Detection
# Practice Project

import re
import sys

# Write the regex to detect the dates in DD/MM/YYYY format
dateRegex = re.compile(r'((\d{2})/(\d{2})/(\d{4}))')

# Write additional code to detect if it is a valid date


def validDate(date_tuple):
    """Determine if date is valid or not by printing helpful text"""
    day = int(groups[1])
    if day < 1 or day > 31:
        print('Invalid day:', groups[1])
        return
    month = int(groups[2])
    if month < 1 or month > 12:
        print('Invalid month')
        return
    year = int(groups[3])
    if year < 1000 or year > 2999:
        print('Invalid year')
        return
    if month in (9, 4, 6, 11):
        if day == 31:
            print(f'Invalid day for 30 day month')
            return
    if month == 2 and day == 29:
        if year % 4 != 0:
            print('Invalid Feb 29 for non leap Year')
            return
        if year % 100 == 0 and year % 400 != 0:
            print('Invalid Feb 29 for non leap Year')
            return
    if month == 2 and day > 29:
        print('Invalid day for Feb')
        return
    print('Valid Date')

text = """
31/02/2020 31/04/2021
00/01/2024 32/01/2024
01/00/2024 01/13/2024
01/01/0999 01/01/3000
31/09/2024 31/04/2024 31/06/2024 31/11/2024
30/02/2024 31/02/2024
29/02/2024 29/02/2023
29/02/1700 29/02/1800 29/02/1900
29/02/2100 29/02/2200 29/02/2300
29/02/2500 29/02/2600 29/02/2700
29/02/2900
"""
for groups in dateRegex.findall(text):
    print('Date matched:', groups[0])
    validDate(groups)
