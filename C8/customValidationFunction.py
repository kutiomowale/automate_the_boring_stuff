#!/usr/bin/env python3
# A default file
""" Passing a Custom Validation Function to

pyinptplus inputCustom() function

"""

import pyinputplus as pyip


def addsUpToTen(numbers):
    """String of digits that adds up to 10

    Args:
        numbers (str): String of digits

    Returns: Int form of numbers if digits in it add up to 10

    Raises:
        Exception if digits in numbers does not add up to 10

    """
    numbersList = list(numbers)
    for i, number in enumerate(numbersList):
        numbersList[i] = int(number)
    if sum(numbersList) != 10:
        text = f'The digits must add up to 10, not {sum(numbersList)}.'
        raise Exception(text)
    return int(numbers)


response = pyip.inputCustom(addsUpToTen)
print(f'***{response}***')
