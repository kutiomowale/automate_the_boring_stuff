#!/usr/bin/env python3
# Find an American Phone Number in a String
# without Regular Expressions


def isPhoneNumber(text):
    """Check whether text matches the pattern of an American Phone Number

    Args:
        text (str): String to check
    Return:
        Bool: True if text matches, otherwise False

    Raises:
        TypeError: If text is not a string

    Examples:
        >>> isPhoneNumber('415-555-4242')
        True
        >>> isPhoneNumber('4155554242')
        False
        >>> isPhoneNumber('Moshi Moshi')
        False
        >>> isPhoneNumber('415-55-4242')
        False
        >>> isPhoneNumber(41555554242)
        Traceback (most recent call last):
        ...
        TypeError: Argument must be a String
    """
    if not isinstance(text, str):
        raise TypeError('Argument must be a String')
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print('Is 415-555-4242 a phone number?')
    print(isPhoneNumber('415-555-4242'))
    print('Is Moshi moshi a phone number?')
    print(isPhoneNumber('Moshi moshi'))
    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            print('Phone number found: ' + chunk)
    print('Done')
