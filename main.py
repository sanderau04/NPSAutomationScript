# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:54:00 2018

@author: Steve Anderau, Alex Markoski, Jonathan Jehring 
"""
import time
import os

def promptUserYN(prompt):
    """Prompt user requiring yes or no input.
    Returns variable input
    """
    input = 'dummy'
    while (input != 'Y' and input !='y' and input != 'N' and input != 'n'):
        input = raw_input('(Answer with Y/N) '+prompt)
    return input

def promptUserEnt(prompt):
    input = 'dummy'
    input = raw_input('(Hit ENTER to continue) '+prompt)
    return input    

def wait(t):
    time.sleep(t)
    return

def openPdf(filename):
    os.system("start "+ filename)
    return

"""
print('Northern Power Systems Power Converter Module Testing Script Initiated'),
time.sleep(1)
print('.'),
time.sleep(1)
print('.'),
time.sleep(1)
print('.')
time.sleep(1)
print('')
"""
raw_input('Press ENTER to continue')
print('')
promptUserYN('I hope this fucking works: ')
promptUserEnt('DO IT')
wait(2)
openPdf('lowPressureAirTest.pdf')


