#!/usr/bin/env python3
# A short program that counts the number counts the number
# of occurrences of each letter in a string.
import pprint
message = ('It was a bright cold day in April, and the clocks were striking'
           ' thirteen.')
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
