#! python3

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # Get addr from cmdl
    address = ' '.join(sys.argv[1:])
else:
    # Get addr from clipboard
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + address)

