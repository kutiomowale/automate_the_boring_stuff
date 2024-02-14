#!/usr/bin/env python3
"""Sandwich Maker

Practice Project

A program that asks users for their sandwich preferences,
and displays a total cost after the user enters their selection.

"""

import pyinputplus as pyip
# For input validation
print('Please select your Sandwich preferences')
my_sandwich = []
# Stores the sandwich preferences of the user
price_list = {
    'wheat': 1000,
    'white': 1000,
    'sourdough': 1000,
    'chicken': 1000,
    'turkey': 1000,
    'ham': 1000,
    'tofu': 1000,
    'cheddar': 500,
    'swiss': 500,
    'mozzarella': 500,
    'mayo': 200,
    'mustard': 200,
    'lettuce': 200,
    'tomato': 200,
    }
# The price list for each option
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], lettered=True,
                       prompt='Select your bread type\n')
my_sandwich.append(bread)
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], lettered=True,
                         prompt='Select your protein type\n')
my_sandwich.append(protein)
if pyip.inputYesNo(prompt='Do you want cheese?\n') == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], lettered=True,
                            prompt='Select your cheese type\n')
    my_sandwich.append(cheese)
if pyip.inputYesNo(prompt='Do you want mayo?\n') == 'yes':
    my_sandwich.append('mayo')
if pyip.inputYesNo(prompt='Do you want Mustard?\n') == 'yes':
    my_sandwich.append('mustard')
if pyip.inputYesNo(prompt='Do you want Lettuce?\n') == 'yes':
    my_sandwich.append('lettuce')
if pyip.inputYesNo(prompt='Do you want Tomato?\n') == 'yes':
    my_sandwich.append('tomato')
number_of_sandwiches = pyip.inputInt(
    prompt='How many sandwiches do you want?\n', min=1)
# How many sandwiches?
total_cost = 0
for content in my_sandwich:
    total_cost += price_list[content]
total_cost *= number_of_sandwiches
# Total cost for the user
print('Thank you.')
print(f'Total cost: ₦{total_cost}')
