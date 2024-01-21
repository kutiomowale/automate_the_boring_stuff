#!/usr/bin/env python3
# 'Comma Code' practice project
import doctest


def commaCode(spam):
    """Return a string of items separated by a comma and a space,

    with and inserted before the last item.

    Args:
        spam (list): A list of strings

    Returns:
        str: The resulting comma separated string

    Examples:
    >>> commaCode(['apples', 'bananas', 'tofu', 'cats'])
    'apples, bananas, tofu, and cats'
    >>> commaCode(['cats'])
    'cats'
    >>> commaCode(['cats', 'dogs'])
    'cats, and dogs'
    >>> commaCode([])
    ''
    >>> commaCode(1)
    Pass only a list of strings
    ''
    >>> commaCode(['cats', 1, 'dogs'])
    Pass only a list of strings
    ''
    """
    if not isinstance(spam, list):
        print('Pass only a list of strings')
        return ''
    if not spam:
        return ''
    for item in spam:
        if not isinstance(item, str):
            print('Pass only a list of strings')
            return ''
    if len(spam) == 1:
        return spam[0]
    res = spam[0]
    SEP = ', '
    for item in spam[1:-1]:
        res = res + SEP + item
    res = res + SEP + 'and ' + spam[-1]
    return res


if __name__ == '__main__':
    doctest.testmod()
