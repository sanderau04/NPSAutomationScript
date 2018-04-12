# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:54:00 2018

@author: Steve Anderau, Alex Markoski, Jonathan Jehring 
"""
import time
import os
import subprocess

def intialize():
    print('Northern Power Systems Power Converter Module Testing Script Initiated'),
    time.sleep(1)
    print('.'),
    time.sleep(1)
    print('.'),
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('')
    raw_input('Press ENTER to continue')
    print('')

def promptUserYN(prompt):
    """Prompt user requiring yes or no input.
    Returns variable input
    """
    input = 'dummy'
    while (input != 'Y' and input !='y' and input != 'N' and input != 'n'):
        input = raw_input(prompt + ' (Answer with Y/N): ')
    return input

def promptUserEnt(prompt):
    input = 'dummy'
    input = raw_input(prompt +' (Press ENTER to continue): ')
    return input    

def wait(t):
    time.sleep(t)
    return

def openPdf(filename):
    subprocess.Popen([filename], shell=True)
    return


# %%
intialize()

# %% Mechanical Connections Test 
promptUserEnt('Insert Module into tray')
promptUserEnt('Ensure Module and tray security before continuing')
promptUserYN('Mechanical Connections finished, continue to low pressure air test?')

# %% Low Pressure Air Test 
lowPressureFile = 'lowPressureAirTest1.pdf'
print ('OPENING FILE: '+lowPressureFile)
openPdf(lowPressureFile)
wait(4)
promptUserEnt('Execute steps 1-3 in section 6 Procedure')
promptUserYN('Continue?')
####AUTOMATION#####
print('TURNING ON AIR COMPRESSOR')
wait(2)
###################
promptUserEnt('Execute step 5 in section 6 Procedure')
pressureAnswer = promptUserYN('Pressure at 10 PSI?')
####AUTOMATION#####
while (pressureAnswer == 'n' or pressureAnswer == 'N'):
    print('RESTARTING AIR COMPRESSOR')
    wait(3)
    pressureAnswer = promptUserYN('Pressure at 10 PSI?')
"""IF no
    Repeat above automation
"""
###################

# %% Electrical Safety Test

# %% Functional EOL Test

# %% High Pressure Coolant Test
