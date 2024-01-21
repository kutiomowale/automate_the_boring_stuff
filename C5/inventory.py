#!/usr/bin/env python3
# Fantasy Game Inventory
# List to Dictionary Function for Fantasy Game Inventory
# Practice Projects
# inventory.py
import doctest


def displayInventory(inventory):
    """Displays a player's inventory

    Args:
        inventory (dict): Where a key is a string
        representing an inventory item,
        and its value is an int representing how many of that item
        the player has.

    Examples:
    >>> displayInventory({'arrow': 12, 'rope': 5})
    Inventory:
    12 arrow
    5 rope
    Total number of items: 17
    >>> displayInventory({})
    Inventory:
    Total number of items: 0
    """
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    """Return a dictionary that represents @inventory
    updated by @addedItems

    Args:
        inventory (dict): A players inventory,
        item(str): item count(int)
        addedItems (list): list of strings to be included
        in new updated inventory

    Returns:
        (dict): The updated dictionary(inventory)

    Examples:
        >>> inve = {'rope': 5, 'torch': 2}
        >>> upd = ['torch', 'dagger', 'torch']
        >>> addToInventory(inve, upd)
        {'rope': 5, 'torch': 4, 'dagger': 1}
        >>> addToInventory(inve, [])
        {'rope': 5, 'torch': 2}
    """
    res = inventory.copy()
    for item in addedItems:
        res.setdefault(item, 0)
        res[item] = res[item] + 1
    return res


if __name__ == '__main__':
    doctest.testmod()

    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventory(stuff)
    print('------------')

    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)
