#!/usr/bin/env python3
# It is an error to try to use a local variable in a function,
# before you assign a value to it.


def spam():
    print(eggs)  # ERROR!
    eggs = 'spam local'


eggs = 'global'
spam()
