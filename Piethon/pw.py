#!/usr/bin/python3

PASSWORDS = {
        'email': 'Purpledrank',
        'blog': 'QWERTYuioPLKj',
        'kelsey': '2klAziel',
        'mum': '14435681'
        }

import sys, pyperclip

if len(sys.argv) < 2:
    print("Usage: python3 pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f"Password for {account} copied to clipboard.")
else:
    print(f"There is no account named {account}")
