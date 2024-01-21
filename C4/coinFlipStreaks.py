#!/usr/bin/env python3
# 'Coin Flip Streaks' practice project
import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    res = ''
    for flips in range(100):
        if random.randint(0, 1):
            res += 'H'
        else:
            res += 'T'
    if 'HHHHHH' in res or 'TTTTTT' in res:
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
