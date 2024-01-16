#!/usr/bin/env python3
# The Collatz Sequence


def collatz(number):
    """Return result if number is even or odd.

    Args:
        number (int): The input

    Returns:
        int: number // 2 if number is even, otherwise 3 * number + 1
    """
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


try:
    val = int(input('Enter number: '))
    while True:
        res = collatz(val)
        if res == 1:
            break
        val = res
except ValueError:
    print('You must enter an integer.')
