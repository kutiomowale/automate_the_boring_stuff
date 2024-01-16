#!/usr/bin/env python3
# Global-statement example


def spam():
    global eggs
    eggs = 'spam'


eggs = 'global'
spam()
print(eggs)
