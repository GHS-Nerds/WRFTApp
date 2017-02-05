#!/usr/bin/python

import os

userinput = input('Yes or No: ')

if userinput == 'Yes':
    os.system("ruby sendmail.rb")
