#!/usr/bin/python

import webbrowser

userinput = input('Yes or No: ')

if userinput == 'Yes':
    webbrowser.open_new("file:///path/to/WRFTApp_email_tests/Browsermode/form.cfm")
