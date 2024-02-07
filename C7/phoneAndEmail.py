#!/usr/bin/env python3
# Phone Number and Email Extractor
# Chapter Project
import re
import pyperclip

# Get text from the Clipboard
text = str(pyperclip.paste())

# Extract phone nos and email addresses
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # area code
    (\s|-|\.)?  # separator
    (\d{3})  # first 3 digits
    (\s|-|\.)  # separator
    (\d{4})  # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  # username
    @ # @ symbol
    [a-zA-Z0-9.-]+  # domain name
    (\.[a-zA-Z]{2,4})  # dot-something
    )''', re.VERBOSE)

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# TODO: Copy this data as a single to the clipboard
if len(matches) > 0:
    pyperclip.paste('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
