#!/usr/bin/env python3
# Keep asking unitil valid age is entered

while True:
    print('Enter your age:')
    try:
        age = int(input())
    except ValueError:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    break

print(f'Your age is {age}.')
