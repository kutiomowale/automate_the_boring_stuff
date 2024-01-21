#!/usr/bin/env python3
# Practice Projects
# Chess Dictionary Validator
# Determine if a Chess Board represented with a dictionary is valid


def isValidChessBoard(board):
    """Return true if @board is a valid chess board

    Args:
        board (dic): A dictionary representing a chess board

    Returns:
        (bool): True if @board is valid, False otherwise

    Raises:
        TypeError: If @board is not a dictionary
        ValueError: If the kaeys and values in @board are not all strings
    Examples:
        >>> isValidChessBoard(1)
        Traceback (most recent call last):
        ...
        TypeError: board must be a dictionary
        >>> isValidChessBoard([])
        Traceback (most recent call last):
        ...
        TypeError: board must be a dictionary
        >>> isValidChessBoard({'1h': 'bking', '3e': 'wking', 24: 'bbishop'})
        Traceback (most recent call last):
        ...
        ValueError: All the keys and values of board must be strings
        >>> isValidChessBoard({'1h': 'bking', '3e': 'wking', '2g': 24})
        Traceback (most recent call last):
        ...
        ValueError: All the keys and values of board must be strings
        >>> isValidChessBoard({'1h': 'bking'})
        False
        >>> isValidChessBoard({})
        False
        >>> cb = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
        ... '5h': 'bqueen', '3e': 'wking'}
        >>> isValidChessBoard(cb)
        True
        >>> cb['1h'] = 'bpawn'
        >>> isValidChessBoard(cb)
        False
        >>> cb['1h'] = 'bking'
        >>> cb['3e'] = 'wpawn'
        >>> isValidChessBoard(cb)
        False
        >>> cb['3e'] = 'wking'
        >>> cb['2g'] = 'bking'
        >>> isValidChessBoard(cb)
        False
        >>> cb['2g'] = 'bbishop'
        >>> cb['6c'] = 'wking'
        >>> isValidChessBoard(cb)
        False
        >>> cb['6c'] = 'wqueen'
        >>> isValidChessBoard(cb)
        True
        >>> cb = {'1h': 'bking', '2g': 'bbishop'}
        >>> isValidChessBoard(cb)
        False
        >>> cb = {'1h': 'wking', '2g': 'wbishop'}
        >>> isValidChessBoard(cb)
        False

    """
    if not isinstance(board, dict):
        raise TypeError('board must be a dictionary')
    for k, v in board.items():
        if not isinstance(k, str) or not isinstance(v, str):
            raise ValueError('All the keys and values of board must be'
                             + ' strings')

    if len(board) < 2 or len(board) > 32:
        return False
    for pos in board:
        if len(pos) != 2:
            return False
        if not (pos[0] >= '1' and pos[0] <= '8'
                and pos[1] >= 'a' and pos[1] <= 'h'):
            return False
    pieces = ('wking', 'wqueen', 'wrook', 'wknight', 'wbishop', 'wpawn',
              'bking', 'bqueen', 'brook', 'bknight', 'bbishop', 'bpawn')
    for piece in board.values():
        if piece not in pieces:
            return False

    black = [v for v in board.values() if v.startswith('b')]
    if len(black) < 1 or len(black) > 16:
        return False
    if black.count('bking') != 1:
        return False
    if black.count('bpawn') > 8:
        return False

    white = [v for v in board.values() if v.startswith('w')]
    if len(white) < 1 or len(white) > 16:
        return False
    if white.count('wking') != 1:
        return False
    if white.count('wpawn') > 8:
        return False

    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    myBoard = {'1a': 'wrook', '1b': 'wknight', '1c': 'wbishop',
               '1d': 'wqueen', '1e': 'wking', '1f': 'wbishop',
               '1g': 'wknight', '1h': 'wrook',
               '2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn',
               '2e': 'wpawn', '2f': 'wpawn', '2g': 'wpawn', '2h': 'wpawn',
               '8a': 'brook', '8b': 'bknight', '8c': 'bbishop',
               '8d': 'bqueen', '8e': 'bking', '8f': 'bbishop',
               '8g': 'bknight', '8h': 'brook',
               '7a': 'bpawn', '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn',
               '7e': 'bpawn', '7f': 'bpawn', '7g': 'bpawn', '7h': 'bpawn'}
    print(isValidChessBoard(myBoard))
