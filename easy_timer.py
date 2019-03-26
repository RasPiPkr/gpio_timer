#! /usr/bin/python3
import subprocess, time, sys, re, os


"""I got the idea for this script for a guy at work who isnt into programming
he was talking about doing a christmas lighting setup for hundreds of lights
and so I created this so he could arrange his own outputs for relays and be a timed
Script created by Martin Parker."""

# Clear the screen for clarity.
os.system('clear')

# Get input of output filename.
try:
    print('Please enter a filename without the .py as it will be added automatically.')
    newScript = input('Using only alphanumeric characters, example: mygpiotimer   : ')
    newScript = str(newScript)

    # Check if newScript has the correct file extension.
    if len(newScript) >= 1 and newScript.isalnum():
        pass
        newScript = newScript + '.py'
    else:
        print('Incorrect output filename')
        print('Cancelling script')
        sys.exit()
    if os.path.isfile(newScript) == True:
        print('\n*** The filename entered already exists in your current directory. ***')
        print('\n*** It will be overwritten with your new timer setup. ***')
        y = int(input('\n\nPress 1 then enter to continue OR anything else then enter to abort: '))
        if y != 1:
            print('\nIncorrect entry, cancelling script:', newScript)
            sys.exit()
except NameError:
    print('***********************************************************************')
    print('********* You may be running wrong python version in terminal *********')
    print('*********           Try sudo python3 easy_timer.py            *********')
    print('********* You may be running wrong python version in terminal *********')
    print('***********************************************************************')
    print('\nIncorrect entry, cancelling script: ', newScript)
    sys.exit()
except ValueError:
    print('\nCancelling script')
    sys.exit()
except KeyboardInterrupt:
    print('\nCancelling script')
    sys.exit()
except SyntaxError:
    print('\nIncorrect entry, cancelling script: ', newScript)
    sys.exit()

time.sleep(1)
os.system('clear')

# Information and warning.
print('*** DISCLAIMER: ***')
print('WARNING: This script will create the following filename:', newScript)
print('If the filename exists it will be destroyed and yours created.')
print('Check this directory as the file will be created here.\n')
print('*** Double check you will be programming the correct BCM outputs. ***')
print('*** If not you may damage your Raspberry Pi or connected equipment. ***')
print('*** I will not be held responsible for your mistakes entering data. ***\n')
print('*** Dont panic, just have to make you aware ***\n')

# if unsure for the filename, a chance to abort.
try:
    y = int(input('Press 1 then enter to continue OR anything else then enter to abort: '))
    if y != 1:
        print('\nIncorrect entry, cancelling script:', newScript)
        sys.exit()
except ValueError:
    print('\nIncorrect entry, cancelling script:', newScript)
    sys.exit()
except NameError:
    print('\nIncorrect entry, cancelling script:', newScript)
    sys.exit()
except KeyboardInterrupt:
    print('\nCancelling script:', newScript)
    sys.exit()
except SyntaxError:
    print('\nIncorrect entry, cancelling script:', newScript)
    sys.exit()

# Clear the screen for clarity.
os.system('clear')

# Explain how to enter data.
print('*****************************')
print('* HOW TO PROGRAM YOUR TIMER *')
print('*****************************')
print('*** IMPORTANT: You will be asked for a BCM, NOT board pin number ***')
print('Each step will consist of the output and then the time for delay.')
print('\nENTERING THE BCM OUTPUTS')
print('Multiple outputs can be triggered together and as many as required.')
print('Example: 7,17,27 (no spaces just with comma seperated values).')
print('Enter 0 to have no outputs triggered for a delay step.')
print('\nENTERING THE DELAYS')
print('Enter the delay time in seconds, decimals allowed.')
print('Examples: 1 OR 0.1 for a faster time and only one delay time.')
print('\n*** Press Ctrl + C to cancel this script if you make a mistake at any time ***\n')

# Setup some variables.
try:
    print('\n*** Timer Configuration ***')
    print('\nPlease enter: 1= loop forever, 2= loop a number of times or 0= only run once. ')
    loop = int(input('How would you like the script to run? '))
    if loop == 1:
        sLoop = True
        sLoop = str(sLoop)
    elif loop == 0:
        sLoop = False
        sLoop = str(sLoop)
    elif loop == 2:
        sLoop = True
        sLoop = str(sLoop)
        loop_num = int(input('How many times to loop through your timer? '))
        if loop_num <= 1:
            print('\nIncorrect entry, cancelling script:', newScript)
            sys.exit()
        else:
            loop_num = str(loop_num)
    else:
        print('\nIncorrect entry, cancelling script:', newScript)
        sys.exit()
    print('\nPlease enter: 1= trigger a high/3.3v OR 0= trigger a low/Gnd/0v.')
    pol = int(input('How would you like the triggering state to be? '))
    if pol == 1:
        p = True
        p = str(p)
    elif pol == 0:
        p = False
        p = str(p)
    else:
        print('\nIncorrect entry, cancelling script:', newScript)
        sys.exit()
    print('\nEach trigger on or off is a step, it may help to have a list prepared.')
    num = int(input('How many steps would you like to take? '))
except ValueError:
    print('\nIncorrect entry, cancelling script:', newScript)
    sys.exit()
except KeyboardInterrupt:
    print('\nCancelling script:', newScript)
    sys.exit()
except NameError:
    print('\nIncorrect entry, cancelling script:', newScript)
    sys.exit()
except SyntaxError:
    print('\nIncorrect entry, cancelling script:', newScript)
    sys.exit()
# Take a breath, ready for how to use information.
time.sleep(2)

# Set some variables.
o = []
t = []
i = 1
y = ()
a = str()

# Clear the screen for clarity.
os.system('clear')

print('If you get stuck scroll up to find instructions.\n')
# get the output and delay time data.
try:
    while i <= num:
        z = i
        z = str(z)
        print(('Step: ') + z)
        a = eval(input('Enter the BCM outputs: '))
        o.append(a)
        b = float(eval(input('Enter the delay time: ')))
        t.append(b)
        i+=1

except KeyboardInterrupt:
    print(('\nCancelling script: ') + newScript)
    sys.exit()

# processing the above data entered for new script to be created.
lo = len(o)
oa = o
oa = str(oa)
oa = oa.replace('[', '')
oa = oa.replace("'", '')
oa = oa.replace(']', '')
o = oa
ta = t
ta = str(ta)
ta = ta.replace('[', '')
ta = ta.replace("'", '')
ta = ta.replace(']', '')
t = ta

# new script creating.
with open(newScript, 'w+') as sScript:
    sScript.write('import RPi.GPIO as GPIO\nimport time\n\n')
    sScript.write('# This whole script was automatically created by another python script called easy_timer.py\n')
    sScript.write('# The initial script was created by Martin Parker.\n\n')
    sScript.write("# Sets the GPIO's outputs to BCM with no warnings.\n")
    sScript.write('GPIO.setmode(GPIO.BCM)\n')
    sScript.write('GPIO.setwarnings(False)\n')
    sScript.write('GPIO.cleanup()\n\n')
    sScript.write('# Default polarity for output.\n')
    sScript.write('on = True\noff = False\n')
    sScript.write('# Check if polarity needs to be negative trigger from filename argument.\n')
    sScript.write('p = ')
    sScript.write(p)
    sScript.write('\nif p == False:\n')
    sScript.write('    on = False\n    off = True\n\n')
    sScript.write('# Outputs\n')
    sScript.write('o = ')
    sScript.write(o)
    sScript.write('\n# Time delay.\n')
    sScript.write('t = ')
    sScript.write(t)
    sScript.write("\nw = ['(',')']\n")
    sScript.write('lo = len(o)\n\n')
    sScript.write('# Sets to be looped or how many times.\n')
    sScript.write('sLoop = ')
    sScript.write(sLoop)
    if loop == 2:
        sScript.write('\nloop_til = ')
        sScript.write(loop_num)
    sScript.write('\n\n')
    sScript.write('# Sets the BCM outputs that was entered.\n')
    sScript.write('def outs():\n')
    sScript.write('    for i in range(lo):\n')
    sScript.write('        if o[i] in list(w):\n')
    sScript.write('            om = o[i]\n')
    sScript.write('            lom = len(om)\n')
    sScript.write('            for ii in range(lom):\n')
    sScript.write('                GPIO.setup(om[i], GPIO.OUT)\n')
    sScript.write('                GPIO.output(om[i], off)\n\n')
    sScript.write('        else:\n')
    sScript.write('            GPIO.setup(o[i], GPIO.OUT)\n')
    sScript.write('            GPIO.output(o[i], off)\n\n')
    sScript.write('# Sets the outputs accordingly with the delay times.\n')
    sScript.write('def timer():\n')
    sScript.write('    for i in range(lo):\n')
    sScript.write('        if o[i] in list(w):\n')
    sScript.write('            om = o[i]\n')
    sScript.write('            lom = len(om)\n')
    sScript.write('            for ii in range(lom):\n')
    sScript.write('                GPIO.output(om[ii], on)\n')
    sScript.write('                time.sleep(t[i])\n')
    sScript.write('            for ii in range(lom):\n')
    sScript.write('                GPIO.output(om[ii], off)\n')
    sScript.write('        GPIO.output(o[i], on)\n')
    sScript.write('        time.sleep(t[i])\n')
    sScript.write('        GPIO.output(o[i], off)\n\n')
    sScript.write('try:\n')
    sScript.write("    print('Starting timer.')\n")
    sScript.write('    if sLoop == True:\n')
    sScript.write('        outs()\n')
    if loop == 2:
        sScript.write('        loop_stop = 0\n')
    sScript.write('        while sLoop == True:\n')
    if loop == 2:
        sScript.write("            loop_stop += 1; print('Loop:', loop_stop, 'of', loop_til)\n")
    sScript.write('            timer()\n')
    if loop == 2:
        sScript.write('            if loop_til == loop_stop:\n')
        sScript.write('                sLoop = False\n')
    sScript.write('    else:\n')
    sScript.write('        outs()\n')
    sScript.write('        timer()\n')
    sScript.write('except KeyboardInterrupt:\n')
    sScript.write('    GPIO.cleanup()\n')
    sScript.write("    print('Exiting Script')\n\n")
    sScript.write("# All done, time to cleanup GPIO's.\n")
    sScript.write('GPIO.cleanup()\nprint("Finished")')
    sScript.close()

# new script finished, enjoy.
time.sleep(1)
print('\nYour timer has been created and is executable.')
subprocess.call('sudo chmod +x {}'.format(newScript), shell=True)
print('To run your timer type: python3', newScript)
print('')
