#!/usr/bin/env python3
# Table Printer Practice Project


def printTable(data):
    """Displays @data in a well-organized table

    with each column right-justified
    Args:
        data (list of lists of strings): The data to display

    Raises:
        ValueError: If data is not a list of lists of strings
    """
    maxLen = 0
    if not isinstance(data, list):
        raise ValueError("Arg must be list of lists of strings")
    for col in data:
        if not isinstance(col, list):
            raise ValueError("Arg must be list of lists of strings")
        for item in col:
            if not isinstance(item, str):
                raise ValueError("Arg must be list of lists of strings")
            if len(item) > maxLen:
                maxLen = len(item)

    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i].rjust(maxLen), end=' ')
        print()


if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)
