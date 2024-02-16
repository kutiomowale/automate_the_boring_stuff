#!/usr/bin/env python3
"""madLibs.py

A program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file.

The results are printed to the screen and saved to a new text file.

"""
import sys
import re
from pathlib import Path

if len(sys.argv) == 1:
    print("Pass text files as command line arguments")
    sys.exit()
for file in sys.argv[1:]:
    p = Path(file)
    if not p.is_file():
        continue
    with open(file) as f:
        words = f.read().split(' ')
    for i in range(len(words)):
        word = words[i]
        if 'ADJECTIVE' in word:
            print("Enter an adjective:")
            res = input()
            words[i] = re.sub(r'ADJECTIVE', res, word)
        elif 'NOUN' in word:
            print("Enter a noun:")
            res = input()
            words[i] = re.sub(r'NOUN', res, word)
        elif 'ADVERB' in word:
            print("Enter an adverb:")
            res = input()
            words[i] = re.sub(r'ADVERB', res, word)
        elif 'VERB' in word:
            print("Enter a verb:")
            res = input()
            words[i] = re.sub(r'VERB', res, word)
    text = ' '.join(words)
    print(text)
    with open(f'{p.stem}_madLib.txt', 'w') as f:
        f.write(text)
