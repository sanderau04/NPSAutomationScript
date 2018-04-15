# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:54:00 2018

@author: Steve Anderau, Alex Markoski, Jonathan Jehring 
"""
import time
import os
import subprocess

def initialize():
    """Starting Animation for master script.
    Does not return anything.
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
    raw_input('Press ENTER to continue')
    print('')

def promptUserYN(prompt):
    """Prompt user requiring yes or no input.
    Returns variable input
    """
    input = 'dummy'
    while (input != 'Y' and input !='y' and input != 'N' and input != 'n'):
        input = raw_input(prompt + ' (Answer with Y/N): ')
    print('')
    return input

def promptUserEnt(prompt):
    """Prompt requiring enter key stroke input
    Does not return anything
    """
    input = 'dummy'
    input = raw_input(prompt +' (Press ENTER to continue): ')
    print('')
    return input    

def wait(t):
    """Cause pause in script for t seconds
    Does not return anything
    """
    time.sleep(t)
    return

def openPdf(filename):
    """Open PDF filename through defualt pdf viewer
    PDF must be 
    Returns filename inputted
    """
    print('OPENING PDF: '+filename)
    wait(3)
    subprocess.Popen([filename], shell=True)
    return filename

def countDown(x):
    """Print count down starting from x
    Does not return anything
    """
    for i in range(x, 0, -1):
        print i, # print in the same line by adding a "," at the end
        time.sleep(1)
    print('')
    return

# %%
initialize()

# %% Mechanical Connections Test 
promptUserEnt('Insert Module into tray')
promptUserEnt('Ensure Module and tray security before continuing')
promptUserYN('Mechanical Connections finished, continue to low pressure air test?')

# %% Low Pressure Air Test 
print('/---------------LOW-PRESSURE-AIR-TEST----------------------------------------/')
pressureInput = 'y'
while pressureInput == 'y' or pressureInput == 'Y': 
    openPdf('LowPressureAirTest.pdf')
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
    
    promptUserEnt('CLOSE VALVE on the pressure testing hose')
    promptUserEnt('START 15 minute pressure test, Computer will prompt you when finished')
    
    #AUTOMATION
    
    wait(2)
    promptUserEnt('PRESSURE TEST FINISHED, no pressure drop was measured')
    pressureInput = promptUserYN('Were there any air pressure leaks heard?')
    if pressureInput == 'y' or pressureInput == 'Y':
      promptUserEnt('Execute step 6 in section 6 Procedure') #modify step 6 in pdf
      print('RESTARTING LOW PRESSURE AIR TEST')
      wait(2)
promptUserEnt('Execute step 8 in section 6 Procedure')
print('END OF LOW PRESSURE AIR TEST')
wait(2)
contElecSafe = promptUserYN('Continue to Electrical Safety Test?')
if contElecSafe == 'n' or contElecSafe == 'N':
    promptUserEnt('Continue when ready')

# %% Electrical Safety Test
print('/-----------------ELECTRICAL-SAFETY-TEST-------------------------------------/')
#ARE THESE initial steps safe? 
promptUserEnt('TURN ON Hi Pot Tester')#get actual
promptUserYN('Hi pot tester on?')

###GROUND CONTINUITY###
openPdf('ElectricalSafetyTest.pdf')
promptUserEnt('Execute section 7.2 in pdf ElectricalSafetyTest.pdf')

###HI POT###
print('RUN TEST SETUP ON HI POTTER')
wait(2)

##AUTOMATION##
print('Running test setup please wait')
wait(3)
#NEED CHECKS TO ENSURE TEST SETUP DONE CORRECTLY
##############

print('test setup finished succesfully')
wait(2)
promptUserEnt('Execute steps 10 and 12 in section 7.3 of ElectricalSafetyTest.pdf')
promptUserEnt('Execute step 14 in section 7.3 of ElectricalSafetyTest.pdf')
promptUserEnt('Execute step 15 and 16 in section 7.3 of ElectricalSafetyTest.pdf')
promptUserEnt('Execute step 17 in section 7.3 of ElectricalSafetyTest.pdf') #possible AUTOMATION for this step
print('INITIATING HI POT TEST, press RED STOP BUTTON at anytime to stop the test')
wait(3)
countDown(5)

#AUTOMATION
#add prompt for stop button (step 21) if unable to automate

ledAnswer = promptUserYN('is the red DANGER LED OFF?')
if ledAnswer == 'y' or ledAnswer == 'Y':
    print('WAIT 1 MINUTE before continuing to INSULATION RESISTANCE TEST, computer will prompt you when one minute has passed')
    wait(2)#CHANGE TO 55 WHEN RUNNING FOREAL
    countDown(5)
    promptUserYN('END OF HI POT TEST. Continue to Insulation Resistance test?')
else:
    print('WAIT 1 MINUTE, computer will prompt you when one minute has passed')
    wait(2)#CHANGE TO 55 WHEN RUNNING FOREAL
    countDown(5)
    promptUserEnt('Execute step 24 in section 7.3 of ElectricalSafetyTest.pdf')
    
    #possible automation of certain parts of step 24 
    #possible user input from step 24

###INSULATION RESISTANCE###
if ledAnswer == 'y' or ledAnswer == 'Y':
    
    ##AUTOMATION UP TO STEP 4##
    print('All test connections are the same as the hi pot test')
    wait(2)
    promptUserEnt('Test setup executed correctly, if error occurs refer to section 7.4 step 5 before continuing')
    ###########################
    
    promptUserEnt('Execute steps 6 and 7 in section 7.4 of ElectricalSafetyTest.pdf')
    
    ##AUTOMATION OF STEP 8 AND 9##
    print('INITIATING INSULATION RESISTANCE')
    wait(1)
    print('The green OFFSET LED should be lit and the red DANGER LED should be flashing indicating that the H.V output is energized')
    wait(5)
    print('press the STOP button at any time if you need to stop the test for any reason')
    wait(3)
    countDown(5)
    ##############################
    
    promptUserEnt('Refer to step 10 in section 7.4 if ElectricalSafetyTest.pdf')
    
    ##AUTOMATION OF STEP 11 and 12##
    print('Reading insulation resistance measurements off of hi potter')
    wait(2)
    print('stopping hi potter')
    wait(2)
    ################################
    
    IRLedAnswer = promptUserYN('Is the red DANGER LED OFF?')
    if IRLedAnswer == 'y' or IRLedAnswer == 'Y':
        promptUserEnt('Execute step 14 in section 7.4 of ElectricalSafetyTest.pdf')
    else:
        promptUserEnt('REFER TO step 15 in section 7.4 of ElectricalSafetyTest.pdf BEFORE continuing')
contFuncEOL = promptUserYN('Continue to Functional EOL Test?')
if contFuncEOL == 'n' or contFuncEOL == 'N':
    promptUserEnt('Continue when ready')
    
    
# %% Functional EOL Test
print('/----------------FUNCTIONAL-EOL-TEST-----------------------------------------/')
openPdf('FunctionalEOLTest.pdf')
promptUserEnt('Read section 1-5 before initiating Functional EOL test script')
wait(2)
print('Initiating Functional EOL Script')
countDown(3)
print('BLEEP BLOOP')
wait(5)
contHighPres = promptUserYN('Continue to High Pressure Coolant Test?')
if contHighPres == 'n' or contHighPres == 'N':
    promptUserEnt('Continue when ready')
# %% High Pressure Coolant Test
print('/-----------------HIGH-PRESSURE-COOLANT-TEST---------------------------------/')
placeHolderPDrop = 'n'
while placeHolderPDrop == 'n' or placeHolderPDrop == 'N': 
    ## Flow and Backflush Test##    
    openPdf('CoolingSystemPressureTest.pdf')
    promptUserEnt('READ THROUGH and execute section 6.1 in CoolingSystemPressureTest.pdf')
    promptUserYN('Continue?')
    
    ## High Pressure Withstand Test##
    print('Initiating High Pressure Withstand Test')
    wait(3)
    
    promptUserEnt('Execute steps 1 and 2 in section 6.2 of CoolingSystemPressureTest.pdf')
    promptUserYN('Continue?')
        
    ####AUTOMATION#####
    print('TURNING ON AIR COMPRESSOR')
    wait(2)
    ###################
        
    promptUserEnt('Execute step 4 in section 6.2 of CoolingSystemPressureTest.pdf')
    ####AUTOMATION####
    print('Computer will prompt you when module is within correct pressure')
    wait(3)
    print('Correct pressure reached, initiating 15 minute pressure drop check')
    countDown(5)
    print('IF LEAK OCCURS during 15 minute pressure drop check execute step 6 in section 6.2 of CoolingSystemPressureTest.pdf')
    wait(5)
    print('Pressure drop check finished')
    ##################
        
    promptUserEnt('Execute step 7 in section 6.2 of CoolingSystemPressureTest.pdf')
    promptUserEnt('Initiate 90 minute pressure test')
        
    ###AUTOMATION###
    print('Running pressure test, time started: BLABLA')
    wait(5)
    promptUserEnt('END OF 90MIN PRESSURE TEST')#beepbeep
    placeHolderPDrop = promptUserYN('PLACE HOLDER press Y for 90min pressure test to have passed, press N for pressure test to have failed')
    ################
    if placeHolderPDrop == 'n' or placeHolderPDrop == 'N':
        promptUserEnt('Execute steps 9 - 12 in section 6.2 of CoolingSystemPressureTest.pdf BEFORE continuing')
        print('RESTARTING Module Cooling System Pressure Test')
    else:
        promptUserEnt('Execute step 13 in section 6.2 of CoolingSystemPressureTest.pdf')
        print('TESTING FINISHED')
