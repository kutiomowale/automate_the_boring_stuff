#!/usr/bin/env python3
# A simple console

welcome_text = 'Welcome to SimCon'

help_text = 'exit to leave\nhelp for help\ncredits for credits'

credit_text = 'SimCon ©kutiomowale 2024.'

prompt_text = '(SimCon) '

print(welcome_text)
print(help_text)

while True:
    print(prompt_text, end='')
    res = input()
    if res == '':
        continue
    elif res == 'help':
        print(help_text)
    elif res == 'credits':
        print(credit_text)
    elif res == 'exit':
        print(credit_text)
        print('Bye')
        break
    else:
        print('Unknown command')
