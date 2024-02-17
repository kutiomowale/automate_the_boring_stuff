#!/usr/bin/env python3
"""Strong Password detection

Practice Project
Using regular expressions to make sure password strings are strong.
A strong password is defined as one that is:
at least eight characters long,
contains both uppercase and lowercase characters,
and has at least one digit.

Also no whitespace(space, tab, newline) charcters.
# I added this condition, not in the book.

"""


def isStrongPassword(password):
    """Determine if string password is a strong password

    It is a strong password if:
    It at least eight characters long,
    Contains both uppercase and lowercase characters,
    And has at least one digit.

    Args:
        password (str): The password

    Return:
        Bool: True if password is strong, False otherwise.

    Raises:
        TypeError: If password is not a string

    Examples:
        >>> isStrongPassword('Aa345678\\n')
        False
        >>> isStrongPassword('Aa345678')
        True
        >>> isStrongPassword('Aa345678 ')
        False
        >>> isStrongPassword('Aa345678  ')
        False
        >>> isStrongPassword('aa345678')
        False
        >>> isStrongPassword('AA345678')
        False
        >>> isStrongPassword('Aaaaaaaa')
        False
        >>> isStrongPassword('Aa34567')
        False
        >>> isStrongPassword('')
        False
        >>> isStrongPassword('        ')
        False
        >>> isStrongPassword('              ')
        False
        >>> isStrongPassword(1)
        Traceback (most recent call last):
        ...
        TypeError: Argument must be a string
    """
    import re
    if not isinstance(password, str):
        raise TypeError("Argument must be a string""")

    if re.search(r'\w{8,}', password) is None:
        return False
    # It at least eight characters long

    if re.search(r'[A-Z]+', password) is None:
        return False
    if re.search(r'[a-z]+', password) is None:
        return False
    # Contains both uppercase and lowercase characters

    if re.search(r'\d+', password) is None:
        return False
    # And has at least one digit.

    if re.search(r'\s+', password) is not None:
        return False
    # No whitespace characters

    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
