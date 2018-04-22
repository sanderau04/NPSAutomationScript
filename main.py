# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:54:00 2018

@author: Steve Anderau, Alex Markoski, Jonathan Jehring 
"""
import time
import os
import subprocess
import datetime
import sys, traceback

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

def contWhenReady(text):
    response = promptUserYN(text)
    if response == 'n' or response == 'N':
        promptUserEnt('Continue when ready')

def main():
    try:
        npsLogo = """

MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds/-`yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmy+-.`````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmho:.``````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdo/.```````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/```````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.```````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmNMMMMMMMMMMMMMMMMMMMm.```````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmho:.`.sNMMMMMMMMMMMMMMMMMm.```````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhs/-.```````-yMMMMMMMMMMMMMMMMm.```````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNdy+-.``````````````:hMMMMMMMMMMMMMMm.```````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNy+:.```````-`````````````/mMMMMMMMMMMMMm.```````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMN-```````````/o`````````````.oNMMMMMMMMMMm.```````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh`````````````s+``````````````.sNMMMMMMMMm.```````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh`````````````.m+```````````````-hMMMMMMMm.```````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh``````````````/N/````````````````:dMMMMMm.```````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh```````````````yN/````````````````.+mMMMm.```````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh```````````````-NN:`````````````````.oNMm.```````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh````````````````+MN:``````````````````-yy.```````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh`````````````````/ho`````````````````````````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh``````````````````:dm-odNdhyso+/-..``````````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh```````````````.+soMM:.://+++ooossso++/-`````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh`````````````.oNMyoMM/```````````````````````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh```````````-sNmo-`oMM+```````````````````````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh`````````-yms:.```oMMo/+`````````````````````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh```````:yy/.``````oMMs/Mh-```````````````````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh`````:o+.`````````oMMy:MMNo.`````````````````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh````.-````````````oMMh-NMMMd:````````````````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh``````````````````oMMd-NMMMMMs.``````````````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh``````````````````oMMm-NMMMMMMm/`````````````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh``````````````````oMMN.mMMMMMMMMy-```````````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh``````````````````oMMN-mMMMMMMMMMN+``````````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh``````````````````oMMN-dMMMMMMMMMMMh-````````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh``````````````````oMMM:hMMMMMMMMMMMMNo.``````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh``````````````````oMMM/yMNNNNNNNNNMMMMd:`````````````````````yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMh`..---::///++++ooossssssssssssssssssssssooooo+++///:::--...``yMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMNmmdhhhysyyhhhdddddmmmmNNNNNNNNMMMMMMMMMMMMMMMNNNNNNNmmmmmddddhhhyysoyhddmmNMMMMMMMMMMMM
MMMMNmmmmdddmmNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmdddddmmNNMMMM
MNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        """
        # %%
        print(npsLogo)
        print('')
        initialize()
        #-------------------------------------------
        # %% Mechanical Connections Test 
        """ Prompt user to put module into tray and check its security
        May need more information added
        """
        print('/---------------MECHANICAL-CONNECTIONS-TEST-------------------------------------------------------------------------/')
        
        promptUserEnt('Insert Module into tray')
        promptUserEnt('Ensure Module and tray security before continuing')
        contWhenReady('Mechanical Connections finished, continue to low pressure air test?')
        
        # %% Low Pressure Air Test 
        """ Step wise approach to low pressure air test 
        Calls on modified low pressure are test procedure PDF 
        Modifications to PDF exclude steps that are now automated
        """
        print('/---------------LOW-PRESSURE-AIR-TEST-------------------------------------------------------------------------------/')
        pressureInput = 'y'
        while pressureInput == 'y' or pressureInput == 'Y': 
            openPdf('LowPressureAirTest.pdf')
            wait(4)
            promptUserEnt('Execute steps 1-3 in section 6 of LowPressureAirTest.pdf')
            contWhenReady('Continue?')
            
            ####AUTOMATION#####
            print('TURNING ON AIR COMPRESSOR')
            wait(2)
            ###################
            
            promptUserEnt('Execute step 5 in section 6 of LowPressureAirTest.pdf')
            pressureAnswer = promptUserYN('Pressure at 10 PSI?')
            
            ####AUTOMATION#####
            while (pressureAnswer == 'n' or pressureAnswer == 'N'):
                promptUserEnt('Execute step 3 in section 6 of LowPressureAirTest.pdf')
                print('RESTARTING AIR COMPRESSOR')
                wait(3)
                pressureAnswer = promptUserYN('Pressure at 10 PSI?')
            """IF no
                Repeat above automation
            """
            ###################
            
            promptUserEnt('Execute Step 6 in section 6 of LowPressureAirTest.pdf')## MODIFY STEP 6?
            promptUserEnt('START 15 minute pressure test, Computer will prompt you when finished')
            
            #AUTOMATION OF 15 MIN PRESSURE TEST (step 6/7)
            
            wait(2)
            promptUserEnt('PRESSURE TEST FINISHED, no pressure drop was measured')
            pressureInput = promptUserYN('Were there any air pressure leaks heard?')
            if pressureInput == 'y' or pressureInput == 'Y':
              promptUserEnt('Execute step NEW STEP in section 6 of LowPressureAirTest.pdf') #MODIFY MAKE NEW STEP (probs make it new step 7, 7 is not needed w/ master script)
              print('RESTARTING LOW PRESSURE AIR TEST')
              wait(2)
        promptUserEnt('Execute step 8 in section 6 of LowPressureAirTest.pdf')
        print('END OF LOW PRESSURE AIR TEST')
        wait(2)
        contWhenReady('Continue to Electrical Safety Test?')
        # %% Electrical Safety Test
        """
        """
        print('/-----------------ELECTRICAL-SAFETY-TEST----------------------------------------------------------------------------/')
        #ARE THESE initial steps safe? 
        promptUserEnt('TURN ON Hi Pot Tester')#Check setup steps, make sure everythings explained
        contWhenReady('Hi pot tester on?')
        
        print('/-----------------ELECTRICAL-SAFETY-TEST:-GROUND-CONTINUITY---------------------------------------------------------/')
        ###GROUND CONTINUITY###
        openPdf('ElectricalSafetyTest.pdf')
        promptUserEnt('Execute section 7.2 in pdf ElectricalSafetyTest.pdf')
        
        print('/-----------------ELECTRICAL-SAFETY-TEST:-HI-POT--------------------------------------------------------------------/')
        ###HI POT###
        promptUserEnt('RUN TEST SETUP ON HI POTTER')
        wait(2)
        
        ##AUTOMATION##
        print('Running test setup please wait')
        wait(3)
        #NEED CHECKS TO ENSURE TEST SETUP DONE CORRECTLY
        ##############
        
        print('test setup finished succesfully')
        print('')
        wait(2)
        promptUserEnt('Execute steps 10 and 12 in section 7.3 of ElectricalSafetyTest.pdf')
        promptUserEnt('Execute step 14 in section 7.3 of ElectricalSafetyTest.pdf')
        promptUserEnt('Execute step 15 in section 7.3 of ElectricalSafetyTest.pdf')
        print('HIGH VOLTAGE ALERT WILL SOUND the High Voltage test is about to begin')
        print('')
        promptUserEnt('Execute step 17 in section 7.3 of ElectricalSafetyTest.pdf') #possible AUTOMATION for this step
        print('INITIATING HI POT TEST, press RED STOP BUTTON at anytime to stop the test')
        wait(3)
        countDown(5)
        
        #AUTOMATION
        #add prompt for stop button (step 21) if unable to automate
        
        ledAnswer = promptUserYN('is the red DANGER LED OFF?')
        if ledAnswer == 'y' or ledAnswer == 'Y':
            ledAnswer2 = promptUserYN('CONFIRM ANSWER: you have submitted that the red DANGER LED is OFF, is this correct?')
        else:
            ledAnswer2 = promptUserYN('CONFIRM ANSWER: you have submitted that the red DANGER LED is ON, is this correct?')
            
        if ((ledAnswer == 'y' or ledAnswer == 'Y') and (ledAnswer2 == 'y' or ledAnswer2 == 'Y')) or ((ledAnswer == 'n' or ledAnswer == 'N') and (ledAnswer2 == 'n' or ledAnswer2 == 'N')):
            print('WAIT 1 MINUTE before continuing to INSULATION RESISTANCE TEST, computer will prompt you when one minute has passed')
            wait(2)#CHANGE TO 55 WHEN RUNNING FOREAL
            countDown(5)
            contWhenReady('END OF HI POT TEST. Continue to Insulation Resistance test?')
            
        else:
            print('WAIT 1 MINUTE, computer will prompt you when one minute has passed')
            wait(2)#CHANGE TO 55 WHEN RUNNING FOREAL
            countDown(5)
            promptUserEnt('Execute step 24 in section 7.3 of ElectricalSafetyTest.pdf')
            
            #possible automation of certain parts of step 24 
            #possible user input from step 24
        
        print('/-----------------ELECTRICAL-SAFETY-TEST:-INSULATION-RESISTANCE-----------------------------------------------------/')
        ###INSULATION RESISTANCE###
        if ((ledAnswer == 'y' or ledAnswer == 'Y') and (ledAnswer2 == 'y' or ledAnswer2 == 'Y')) or ((ledAnswer == 'n' or ledAnswer == 'N') and (ledAnswer2 == 'n' or ledAnswer2 == 'N')):
            
            ##AUTOMATION UP TO STEP 4##
            print('All test connections are the same as the hi pot test')
            wait(2)
            promptUserEnt('Setup executed correctly, if error occurs refer to section 7.4 step 5 before continuing')
            ###########################
            
            promptUserEnt('Execute steps 6 in section 7.4 of ElectricalSafetyTest.pdf')
            promptUserEnt('Pressing ENTER will sound the HIGH VOLTAGE ALERT')
            
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
            
            IRledAnswer = promptUserYN('is the red DANGER LED OFF?')
            if IRledAnswer == 'y' or IRledAnswer == 'Y':
                IRledAnswer2 = promptUserYN('CONFIRM ANSWER: you have submitted that the red DANGER LED is OFF, is this correct?')
            else:
               IRledAnswer2 = promptUserYN('CONFIRM ANSWER: you have submitted that the red DANGER LED is ON, is this correct?')
            if ((IRledAnswer == 'y' or IRledAnswer == 'Y') and (IRledAnswer2 == 'y' or IRledAnswer2 == 'Y')) or ((IRledAnswer == 'n' or IRledAnswer == 'N') and (IRledAnswer2 == 'n' or IRledAnswer2 == 'N')):
                promptUserEnt('Execute step 14 in section 7.4 of ElectricalSafetyTest.pdf')
            else:
                promptUserEnt('REFER TO step 15 in section 7.4 of ElectricalSafetyTest.pdf BEFORE continuing')
        contWhenReady('Continue to Functional EOL Test?')
            
        # %% Functional EOL Test
        print('/----------------FUNCTIONAL-EOL-TEST--------------------------------------------------------------------------------/')
        openPdf('FunctionalEOLTest.pdf')
        promptUserEnt('Read section 1-SOMETHING before initiating Functional EOL test script')#MODIFY SETUP
        wait(2)
        print('Initiating Functional EOL Script')
        countDown(3)
        print('BLEEP BLOOP')
        wait(5)
        contHighPres = promptUserYN('Continue to High Pressure Coolant Test?')
        if contHighPres == 'n' or contHighPres == 'N':
            promptUserEnt('Continue when ready')
        # %% High Pressure Coolant Test
        print('/---COOLING-SYSTEM-PRESSURE-TEST------------------------------------------------------------------------------------/')
        print('')
        placeHolderPDrop = 'n'
        while placeHolderPDrop == 'n' or placeHolderPDrop == 'N': 
            print('/---COOLING-SYSTEM-PRESSURE-TEST:-FLOW-TEST-&-BACKFLUSH-------------------------------------------------------------/')
        
            ## Flow and Backflush Test##    
            openPdf('CoolingSystemPressureTest.pdf')
            promptUserEnt('READ THROUGH and execute section 6.1 in CoolingSystemPressureTest.pdf')
            contWhenReady('Continue?')
            
            print('/---COOLING-SYSTEM-PRESSURE-TEST:-HIGH-PRESSURE-WITHSTAND-TEST------------------------------------------------------/')
            ## High Pressure Withstand Test##
            print('Initiating High Pressure Withstand Test')
            wait(3)
            
            promptUserEnt('Execute steps 1 and 2 in section 6.2 of CoolingSystemPressureTest.pdf')
            contWhenReady('Continue?')
                
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
            dateTime90MinPTestStart = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print('Running pressure test, time started: '+dateTime90MinPTestStart)
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
    except KeyboardInterrupt:
        print "Shutdown requested...exiting"
        print 'Input functions to turn off instruments and close communication'
    except Exception:
        print ''
        print 'Input functions to turn off insturments and close communication'
        promptUserEnt('Press ENTER to shutdown all instruments')
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()


