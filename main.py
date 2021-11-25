#inports########################################################################
import time
import os
score = 0
#gets username##################################################################
print("\033[1;31;40mHello, please enter your UserName?")
userName = input("\033[1;37;40m")
#functions######################################################################
def next():
    nex = input("\033[1;32;40mPress Enter To Continue")
    if nex == '':
        pass
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
#start of topic 1###############################################################
clearConsole()
print(f"\033[1;31;40mOkay {userName} let's get started, our first topic is US World History")
time.sleep(3)
next()
#question 1#####################################################################
clearConsole()
print("\033[1;31;40m                                               Topic 1 Qestion 1")####
time.sleep(2)
print("\033[1;31;40mWho was the first US president?")
question1 = input("\033[1;37;40m")
if question1.lower() == "george washington":
    print("\033[1;31;40mThat one was easy +5 points")
    score += 5
elif question1 == '5371':
    pass
else:
    print("\033[1;31;40m\nWrong, the first US president was George Washington")
time.sleep(3)
next()
#question 2#####################################################################
clearConsole()
print("\033[1;31;40m                                               Topic 1 Qestion 2")####
time.sleep(2)
print('\033[1;31;40m\nWhat year did the US declare independence')
question2 = input('\033[1;37;40m')

if question2 == '1776':
    print("\033[1;31;40mnice +5 points")
    score += 5
elif question2 == '5371':
    pass
else:
    print('\033[1;31;40m\nWrong, the correct answer is 1776')
next()
#question 3#####################################################################
clearConsole()
print("\033[1;31;40m                                               Topic 1 Qestion 3")
time.sleep(2)
print("\033[1;31;40m\nWhat year did the US enter WWII")
question3 = input("\033[1;37;40m")

if question3 == "1941":
    print("\033[1;31;40mCorrect, +10 points")
    score += 10
elif question3 == '5371':
    pass
else:
    print("\033[1;31;40mOops, the correct date is actually 1941")
next()
clearConsole()
#topic 2########################################################################
print("\033[1;31;40mOkay thats enough of US history new topic time, and the new topic is\n\ndrumroll please")
time.sleep(3)
print("\033[1;33;40m\n\nMovies!")

#topic 2 question 1
clearConsole()
print("                                                            Topic 2 Qestion 1")
time.sleep(2)
print('\033[1;31;40m\nOkay our first question for this new topic is what is the higest earning movie to date')
nq1 = input("\033[1;37;40m")

if nq1.lower() == 'avatar':
    print("\033[1;31;40mCorrect! Avengers End Game is th....")
    time.sleep(3)
    print("\033[1;31;40mWait its Avatar!?!? I thought it was endgame")
