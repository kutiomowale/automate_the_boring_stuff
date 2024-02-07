#!/usr/bin/env python3
# Practice Questions 20, 21, and 22

import re

# Uncomment ro for the question you need, comment out others

# ro = re.compile(r'^((\d{1}(,\d{3})+)|(\d{1,3}))$')
# Question 20

# ro = re.compile(r'^(([A-Z]+[a-zA-Z]*) Watanabe)$')
# Questiob 21

ro = re.compile(r'''^(
    (Alice|Bob|Carol)        # first word is any of these
    \s+
    (eats|pets|throws)       # second word is any of these
    \s+
    (apples|cats|baseballs)  # third word is any of these
    \.                       # ends with a period
    )$''', re.VERBOSE | re.IGNORECASE)
# Question 22

while True:
    text = input('Enter text to match(nothing to exit):\n')
    if text == '':
        break
    mo = ro.search(text)
    if mo:
        print('Match:', mo.group())
    else:
        print('No match')
