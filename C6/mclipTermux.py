#!/usr/bin/env python3
# mclipTermux.py - A multi-clipboard program - Termux version
import sys
import subprocess

TEXT = {'agree': """Yes I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:
    print('Usage: python myclipTermux.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]  # first command line arg is keyphrase

if keyphrase in TEXT:
    subprocess.run(['termux-clipboard-set', TEXT[keyphrase]])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
