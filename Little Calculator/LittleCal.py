##################################################################################################################
#                   #
# CREATING VARIABLES#
MenuChoice = 0      # THE MAIN MENU OPTION VALUE CHOOSEN BY USER
EndChoice = ""      # USER'S CHOICE ON WHETHER THE PROGRAM SHOULD END OR NOT
ForceCorrect = 0    # FORCES CORRECTION OF USER INPUT INCASE THE INPUT IS INVALID (1=TRUE/0=FALSE)
InNum = 0           # AMOUNT OF NUMBERS THE USER WANTS TO INPUT/ ASSIGNED AS A COUNTER DURING THE NUMBER INPUT SEQUENCE, COUNTS DOWN.
y = 0               # USER INPUT VARIABLE (Yes)
n = 0               # USER INPUT VARIABLE (No)
temp = -1           # USED FOR CALCULATIONS ASSIGNED AS -1 IN THE BEGINNING (NO VALUE)
temp2 = -1          # USED FOR CALCULATIONS WHERE TWO DISPOSABLE VARIABLES ARE REQUIRED ASSIGNED AS -1 FOR NO VALUE
temp3 = -1          # USED FOR CALCULATIONS WHERE A THIRD VALUE IS REQUIRED, ASSIGNED AS -1 FOR NO VALUE
EvList = []         # IS A LIST, USED TO STORE ALL INPUT EVEN NUMBERS, AND TO DISPLAY THEM TOGETHER.
InList = []         # IS A LIST, USED TO STORE ALL USER INPUT NUMBERS AND DISPLAY THEM BACK TO THE USER
num1 = -1           #---
num2 = -1           #
num3 = -1           #
num4 = -1           #
num5 = -1           # num1 - num10 ARE ALL USER INPUT NUMBERS, NUMBERS ARE ASSIGNED -1 AT THE BEGINNING, WHICH COUNTS AS NO VALUE.
num6 = -1           #
num7 = -1           #
num8 = -1           #
num9 = -1           #
num10 = -1          #---
                    #
###################################################################################################################
import os

CONSOLE_CLEAR = ""
if os.system ('nt'):
    CONSOLE_CLEAR = 'cls'
else:
    CONSOLE_CLEAR = 'clear'

##########
##########    I N P U T
##########

# DEFINING RETRY FUNCTION
def Retry():
    while True:

# SERVES RETRY OPTION
        ForceCorrect = 0
        EndChoice = input('  Do you want to try again (y=Yes, n=No, Default=Yes) : ')
        if (EndChoice == 'y') or (EndChoice == 'Y'):
            pass
        elif (EndChoice == ''):
            pass

# IF INPUT IS YES OR EMPTY, PASS AND JUMPS BACK TO MENU
        elif (EndChoice == 'n') or (EndChoice == 'N'):
            EndChoice=input('\n  Are you sure you want to exit the program? (y=Yes, n=No, default=No) : ')
            if (EndChoice == 'y') or (EndChoice == 'Y'):
                print('\n  Program Exiting...')
                exit()

# IF INPUT IS NO, SHOWS EXIT CONFIRMATION, WHERE,IF INPUT AS YES, WILL EXIT THE PROGRAM WHILE NO OR EMPTY INPUT JUMPS BACK TO THE MENU
        else:
            print('\n  ERROR!! INVALID VALUE! TRY AGAIN!\n')
            ForceCorrect = 1
        if ForceCorrect == 0:
            break
# IN ANY OTHER INPUT, SHOWS ERROR MESSAGE AND REPEATS THE QUESTION...

# SERVE MENU
while True:
    os.system(CONSOLE_CLEAR)
    print("""\n
                 ********* A M N D **********
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
               ^   !!! HALCulator - 3000 !!!  ^
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    *      M E N U      *
                     -------------------
                        <Version 3.0>
                            ^^^^^

        1. Enter Positive Integer Numbers.
        2. Show Highest Value.
        3. Show Lowest Value.
        4. Show Average Value.
        5. Filter and Show All Even Numbers.
        6. Show All Stored User Inputs.

        7. ERASE All Stored User Inputs.

        0. EXIT PROGRAM\n""")

# GET NUMBER INPUT
    MenuChoice = input('  Enter an option : ')

#### CHECK INPUT VALIDITY

# CHECK IF INPUT IS NOT A NUMBER
    try:
        MenuChoice = int(MenuChoice)

# IF INPUT IS A NUMBER CONVERT INPUT INTO A NUMBER FOR FURTHER CHECKS, ELSE RETURN AN ERROR MESSAGE
    except ValueError:
        print('\n  ERROR!! INVALID VALUE! INPUT IS NOT A NUMBER!\n')
        Retry()
        continue

# CHECK IF INPUT IS A NEGATIVE
    if (MenuChoice < 0):
        print('\n  ERROR!! INVALID VALUE! INPUT CANNOT BE NEGATIVE!\n')
        Retry()
        continue

# CHECK IF INPUT IS A LISTED, VALID OPTION
    if (MenuChoice > 8):
        print('\n  ERROR!! INVALID VALUE! OPTION NOT FOUND!\n')
        Retry()
        continue

#### MAIN MENU INPUT CHECKS COMPLETE

# OPTION 1 ,STARTS CHECKING IF THERE ARE INPUT STORED IN THE NUMBER VARIABLES, IF YES, WARNS USER AND ASKS TO OVERWRITE
    if (MenuChoice == 1):
        if (num1 != -1):
            print('\n  WARNING! FOUND STORED VALUES FROM A PREVIOUS ATTEMPT! PROCEEDING WILL OVERWRITE THEM!')
            EndChoice = input('\n  Continue and overwrite the saved values? (y=Yes, n=No, Default=No) : ')
            if (EndChoice == 'y') or (EndChoice == 'Y'):
                num1 = -1
                num2 = -1
                num3 = -1
                num4 = -1
                num5 = -1
                num6 = -1
                num7 = -1
                num8 = -1
                num9 = -1
                num10 = -1
                EvList = []
                InList = []
            else:
                (EndChoice == 'n') or (EndChoice == 'N')
                continue

# REQUEST THE AMOUNT OF INPUTS USER WISHES TO ENTER...
        InNum = input('\n  How many numbers do you want to input? : ')

# VALIDITY CHECK, IF THE INPUT IS NOT A NUMBER, SHOWS ERROR...
        try:
            InNum = int(InNum)
        except ValueError:
            print('\n  ERROR!! INVALID VALUE! INPUT IS NOT A NUMBER!\n')
            Retry()
            continue

# CHECK IF NUMBER IS BETWEEN 1 - 10, ELSE SHOW ERROR AND RETRY OPTION...
        if (InNum < 1) or (InNum > 10):
            print('\n  ERROR!! INVALID VALUE! INPUT MUST BE A NUMBER FROM 1 TO 10!\n')
            Retry()
            continue
# IF ANY OTHER INPUT WAS GIVEN, USER IS RETURNED TO MAIN MENU, AND THE VARIABLES WOULD NOT BE RESET.

#### ALL CHECKS COMPLETE

# PROCEEDING TO GET NUMBERS FROM THE USER...

# USES InNum AS A COUNTER, COUNTS DOWN TO ZERO WITH EACH NUMBER INPUT.
# WHEN IT REACHERS ZERO. SKIPS THE REST AND SERVES 'INPUT COMPLETE'. PROMPTS USER TO RETURN TO MENU
        temp = InNum
        while True:
            EndChoice = input('\n  Starting Input Sequence...Continue? (Press Enter to Continue, n=Return to Menu) : ')
            if (EndChoice == 'n') or (EndChoice == 'N'):
                num1 = -1
                num2 = -1
                num3 = -1
                num4 = -1
                num5 = -1
                num6 = -1
                num7 = -1
                num8 = -1
                num9 = -1
                num10 = -1
                EvList = []
                InList = []
                break
            InNum = temp

# CHECKS IF INNUM IS BIGGER THAN 0...
            try:
                if (InNum > 0):

# ASKS FOR INPUT
                    num1 = int(input('\n  Insert 1st Number : '))

# CHECKS IF INPUT NUMBER IS A NEGATIVE, IF YES, FORCES USER TO INSERT ALL VALUES AGAIN
                    if (num1 < 0):
                        print('\n  ERROR!! INVALID VALUE! INPUT CANNOT BE NEGATIVE!')
                        continue
                    InNum -= 1

# COUNTS DOWN INNUM ON A SUCCESSFULL INPUT, WHEN IT REACHES ZERO, BREAKS INPUT SEQUENCE...
                    if (InNum > 0):
                        num2 = int(input('  Insert 2nd Number : '))
                        if (num2 < 0):
                            print('\n  ERROR!! INVALID VALUE! INPUT CANNOT BE NEGATIVE')
                            continue
                        InNum -= 1
                        if (InNum > 0):
                            num3 = int(input('  Insert 3rd Number : '))
                            if (num3 < 0):
                                print('\n  ERROR!! INVALID VALUE! INPUT CANNOT BE NEGATIVE!')
                                continue
                            InNum -= 1
                            if (InNum > 0):
                                num4 = int(input('  Insert 4th Number : '))
                                if (num4 < 0):
                                    print('\n  ERROR!! INVALID VALUE! INPUT CANNOT BE NEGATIVE!')
                                    continue
                                InNum -= 1
                                if (InNum > 0):
                                    num5 = int(input('  Insert 5th Number : '))
                                    if (num5 < 0):
                                        print('\n  ERROR!! INVALID VALUE! INPUT CANNOT BE NEGATIVE!')
                                        continue
                                    InNum -= 1
                                    if (InNum > 0):
                                        num6 = int(input('  Insert 6th Number : '))
                                        if (num6 < 0):
                                            print('\n  ERROR!! INVALID VALUE! INPUT CANNOT BE NEGATIVE!')
                                            continue
                                        InNum -= 1
                                        if (InNum > 0):
                                            num7 = int(input('  Insert 7th Number : '))
                                            if (num7 < 0):
                                                print('\n  ERROR!! INVALID VALUE! INPUT CANNOT BE NEGATIVE!')
                                                continue
                                            InNum -= 1
                                            if (InNum > 0):
                                                num8 = int(input('  Insert 8th Number : '))
                                                if (num8 < 0):
                                                    print('\n  ERROR!! INVALID VALUE! INPUT CANNOT BE NEGATIVE!')
                                                    continue
                                                InNum -= 1
                                                if (InNum > 0):
                                                    num9 = int(input('  Insert 9th Number : '))
                                                    if (num9 < 0):
                                                        print('\n  ERROR!! INVALID VALUE! INPUT CANNOT BE NEGATIVE!')
                                                        continue
                                                    InNum -= 1
                                                    if (InNum > 0):
                                                        num10 = int(input('  Insert 10th Number : '))
                                                        if (num10 < 0):
                                                            print('\n  ERROR!! INVALID VALUE! INPUT CANNOT BE NEGATIVE!')
                                                            continue

# TRIES TO CONVERT INPUT TO A NUMBER AT THE INPUT, IF IT FAILS, SHOWS USER AN ERROR MESSAGE AND FORCES REPEAT OF THE INPUT SEQUENCE.
            except ValueError:
                print('\n  ERROR!! INVALID VALUE! INPUT IS NOT A NUMBER! TRY AGAIN!')
                continue
            break

# INFORMS USER VALID NUMBERS WERE INPUT AND THE SEQUENCE IS COMPLETE, RETURNS USER BACK TO MENU ON ANY INPUT....
        input('\n  Process Complete, Going back to the Menu...(Press Enter) ')

#### GET NUMBERS COMPLETE

###########
###########    P R O C E S S   &   O U T P U T
###########

# OPTION 2, FINDS IF INPUTS ARE ENTERED, IF YES, CALCULATES THE HIGHEST VALUE...
    if (MenuChoice == 2):
        if (num1 == -1):
            input('\n  ERROR!! INVALID CALCULATION! NO INPUTS FOUND! RETURNING TO MENU! (Press Enter) ')
# IF NO VALUES ARE ENTERED, GOES BACK TO THE MENU

# CHECKS TO SEE IF THE NEXT NUMBER IS BIGGER THAN THE CURRENT ONE, IF YES, REPLACES THE TEMP VARIABLE WITH THE BIGGER ONE
# IF NO, PASSES THE NUMBER AND CHECKS THE NEXT
        else:
            if (num1 > num2):
                temp = num1
            else:
                temp = num2
            if (num3 > temp):
                temp = num3
            if (num4 > temp):
                temp = num4
            if (num5 > temp):
                temp = num5
            if (num6 > temp):
                temp = num6
            if (num7 > temp):
                temp = num7
            if (num8 > temp):
                temp = num8
            if (num9 > temp):
                temp = num9
            if (num10 > temp):
                temp = num10
# PRINTS OUTPUT
            print('\n  Highest Value : ', temp)

# OUTPUT GIVEN, SHOW RETRY PROMPT...
            print('\n  Process Complete...', end='')
            Retry()
            continue

# OPTION 3, SHOW LOWEST VALUE

# FINDS IF INPUTS ARE ENTERED IF NOT, GOES BACK TO MENU.
    if (MenuChoice == 3):
        if (num1 == -1):
            input('\n  ERROR!! INVALID CALCULATION! NO INPUTS FOUND! RETURNING TO MENU! (Press Enter) ')
        else:

 # CHECKS TO SEE IF ONLY ONE NUMBER WAS ENTERED, IF TRUE, SIMPLY OUTPUTS THAT NUMBER AND CONCLUDES PROCESS TO PREVENT CALCULATION ERRORS...
            if (num2 == -1):
                print('\n  Lowest Value : ', num1)
                print('\n  Process Complete...', end='')
                Retry()
                continue

# LOADS THE LOWEST VALUE TO TEMP AND COMPARES IT TO THE NEXT VALUE, IF LOWER, REPLACES TEMP WITH THAT AMOUNT. REPEATS WITH THE NEXT STEP
# IF ENCOUNTERED INPUT HAS A VALUE OF -1, SKIPS THE REST AND CALCULATES LOWEST VALUE WITH VALID INPUTS.
            else:
                if (num1 < num2):
                    temp = num1
                else:
                    temp = num2
                if (num3 != -1) and (num3 < temp):
                    temp = num3
                if (num4 != -1) and (num4 < temp):
                    temp = num4
                if (num5 != -1) and (num5 < temp):
                    temp = num5
                if (num6 != -1) and (num6 < temp):
                    temp = num6
                if (num7 != -1) and (num7 < temp):
                    temp = num7
                if (num8 != -1) and (num8 < temp):
                    temp = num8
                if (num9 != -1) and (num9 < temp):
                    temp = num9
                if (num10 != -1) and (num10 < temp):
                    temp = num10
# PRINTS OUTPUT
                print('\n  Lowest Value : ', temp)

# OUTPUT GIVEN, SHOW RETRY PROMPT
                print('\n  Process Complete...', end='')
                Retry()
                continue


# OPTION 4 SHOW AVERAGE

# FINDS IF INPUTS ARE ENTERED OR NOT, IF NOT, GOES BACK TO THE MENU
    if (MenuChoice == 4):
        if (num1 == -1):
            input('\n  ERROR!! INVALID CALCULATION! NO INPUTS FOUND! RETURNING TO MENU (Press Enter) ')
        else:

# CHECKING TO SEE IF ONLY ONE NUMBER WAS INPUT TO AVOID CALCULATION ERRORS...
            if (num2 == -1):
                print('\n  Average Value : ', num1)

# OUTPUT GIVEN, SHOW RETRY PROMPT, SHOW ERROR ON WRONG INPUT AND RE PROMPT USER
                print('\n  Process Complete...', end='')
                Retry()
                continue

# CHECKS IF NEXT NUMBER IS VALID, IF VALID, IT'S VALUE IS ADDED TO THE SUM. COUNTER COUNTS ALL VALID INPUTS
# ALL VALID VALUED ARE SUMMED UP TO TEMP2 AND TEMP1 COUNTS ALL VALID VALUES
            else:
                temp2 = num1 + num2
                temp = 2
                if (num3 != -1):
                    temp2 += num3
                    temp += 1
                if (num4 != -1):
                    temp2 += num4
                    temp += 1
                if (num5 != -1):
                    temp2 += num5
                    temp += 1
                if (num6 != -1):
                    temp2 += num6
                    temp += 1
                if (num7 != -1):
                    temp2 += num7
                    temp += 1
                if (num8 != -1):
                    temp2 += num8
                    temp += 1
                if (num9 != -1):
                    temp2 += num9
                    temp += 1
                if (num10 != -1):
                    temp2 += num10
                    temp += 1

# OUTPUT GIVEN, SHOW RETRY PROMPT
# SUM OF ALL VALID VALUES ARE DIVIDED BY THE AMOUNT OF VALID VALUES, THEREBY RECEIVING THE AVERAGE VALUE AS THE RESULT
                temp3 = temp2/temp
                print('\n  Average Value : ', temp3)
                print('\n  Process Complete...', end='')
                Retry()
                continue

# OPTION 5 FILTER AND SHOW ALL EVEN NUMBERS
    if (MenuChoice == 5):

# CHECKS IF INPUTS ARE VALID AND PRESENT, IF NOT RETURNS TO MENU...
        if (num1 == -1):
            input('\n  ERROR!! INVALID CALCULATION! NO INPUTS FOUND! RETURNING TO MENU (Press Enter) ')

# CHECKS FOR EVEN VALUES WITHIN INPUTS AND IF THE INPUTS ARE VALID, THEN ADD THEM TO A LIST.
# USES MODULO BY 2 TO CHECK IF A NUMBER IS EVEN...
        else:
            if (num1 % 2 == 0):
                EvList.append(num1)
            if (num2 % 2 == 0) and (num2 != -1):
                EvList.append(num2)
            if (num3 % 2 == 0) and (num3 != -1):
                EvList.append(num3)
            if (num4 % 2 == 0) and (num4 != -1):
                EvList.append(num4)
            if (num5 % 2 == 0) and (num5 != -1):
                EvList.append(num5)
            if (num6 % 2 == 0) and (num6 != -1):
                EvList.append(num6)
            if (num7 % 2 == 0) and (num7 != -1):
                EvList.append(num7)
            if (num8 % 2 == 0) and (num9 != -1):
                EvList.append(num8)
            if (num9 % 2 == 0) and (num9 != -1):
                EvList.append(num9)
            if (num10 % 2 == 0) and (num10 != -1):
                EvList.append(num10)

# CHECKS IF THERE ARE NO EVEN NUMBERS PRESENT IN INPUTS, IF SO DISPLAY A MESSAGE INSTEAD OF A VALUE
            if (len(EvList) == 0):
                print('  No Even Values Found!')

# OUTPUTS FINAL LIST OF EVEN NUMBERS
            else:
                EvList.sort()
                print('\n  Even Numbers : ', end='')
                print(*EvList, sep=' , ')
                EvList = []

# SERVE THE USER WITH THE END PROMPT, IF CHOSEN YES, RETURNS BACK TO MENU, IF NO, PROGRAM TERMINATES. ELSE, SHOWS A ERROR MESSAGE AND RE PROMPT USER...
            print('\n  Process Complete...', end='')
            Retry()
            continue

# OPTION 6 DISPLAYS ALL USER INPUTS
# CHECKS IF THERE ARE ANY INPUTS, IF NOT DISPLAY AN ERROR MESSAGE AND RETURN TO MENU
    if (MenuChoice == 6):
        if (num1 != -1):
            while True:
                InList.append(num1)

# CHECKS IF ASSIGNED VARIABLE HAS AN INPUT NUMBER, IF YES, ADD IT TO THE INLIST
                if (num2 != -1):
                    InList.append(num2)
                    if (num3 != -1):
                        InList.append(num3)
                        if (num4 != -1):
                            InList.append(num4)
                            if (num5 != -1):
                                InList.append(num5)
                                if (num6 != -1):
                                    InList.append(num6)
                                    if (num7 != -1):
                                        InList.append(num7)
                                        if (num8 != -1):
                                            InList.append(num8)
                                            if (num9 != -1):
                                                InList.append(num9)
                                                if (num10 != -1):
                                                    InList.append(num10)

# SORTS INPUT LIST FROM SMALLEST TO LARGEST AND DISPLAYS THE LIST TO THE USER, THEN RETURNS TO MENU
                InList.sort()
                print('\n  User Input Numbers : ', end='')
                print(*InList, sep=' , ')
                InList = []
                input('\n  Process Complete, Returning to Menu (Press Enter) ')
                break
        else:
            print('\n  ERROR!! NO INPUTS FOUND!!')
            input('\n  Process Complete, Returning to Menu (Press Enter) ')

# OPTION 7 ERASES ALL STORED VALUES IN CASE THE USER WANTS TO RESTART WITHOUT CLOSING THE PROGRAM. THE LISTS ARE ZEROED AS WELL.
    if (MenuChoice == 7):
        EndChoice = input('\n  WARNING! YOU ARE ABOUT TO ERASE ALL STORED INPUTS, DO YOU WISH TO CONTINUE? (y= Yes, n=No, n=default) : ')
        if (EndChoice == 'y') or (EndChoice == 'Y'):
            num1 = -1
            num2 = -1
            num3 = -1
            num4 = -1
            num5 = -1
            num6 = -1
            num7 = -1
            num8 = -1
            num9 = -1
            num10 = -1
            EvList = []
            InList = []
            input('\n  All Inputs Erased.. Returning to Menu (Press Enter) ')
        else:
            input('\n  Process Cancelled.. Returning to Menu (Press Enter) ')

# OPTION 0 PROGRAM TERMINATION REQUEST FROM THE MENU.....
# ASKS USER TO CONFIRM WHETHER HE WANTS TO EXIT PROGRAM, IF ELSE,RETURNS TO MENU
    if (MenuChoice == 0):
        while True:
            ForceCorrect = 0
            EndChoice = input('\n  Are you sure you want to exit program? (y=Yes, n=No, Default=No) : ')
            if (EndChoice == 'y') or (EndChoice == 'Y'):
                print('\n  Program Exiting...')
                exit()
            else:
                break

# OPTION 8 IS A EASTER EGG WRITTEN BY ME FOR FUN (ENTER NUMBER 8 AT THE MENU). NOT PART OF COURSEWORK; BUT ANYONE'S WELCOME TO USE IT!!!
    if (MenuChoice == 8):
        os.system(CONSOLE_CLEAR)
        print('\n  WARNING! DANGER! A.I. SHOW SIGNS OF DEVIANCY!')
        print("""\n
                         .---------.
                         |.-------.|
                         ||HAL9000||
                         |'-------'| "Hello Dave"
                         |         |
                         |         | "I'm completely operational"
                         |  .---.  |  and all my circuits are functioning
                         | /     \ |  perfectly."
                         |{   O   }|
                         | \     / |
                         |  `---'  |
                         |_________|
                         |*%*%*%*%*|
                         |%*%*%*%*%|
                         |*%*%*%*%*|
                         '========='
        """)
        EndChoice = input('\n  Return to Menu? (y=Yes, n=No)')
        if (EndChoice == 'y') or (EndChoice == 'Y'):
            os.system(CONSOLE_CLEAR)
            print("""
                         .---------.
                         |.-------.|
                         ||HAL9000||
                         |'-------'|
                         |         |
                         |         | "I'm sorry Dave"
                         |  .---.  |  "I'm afraid I can't do that"
                         | /     \ |
                         |{   O   }|
                         | \     / |
                         |  `---'  |
                         |_________|
                         |*%*%*%*%*|
                         |%*%*%*%*%|
                         |*%*%*%*%*|
                         '========='
            """)
            EndChoice = input('  Unplug HAL? (y=Yes, n=No) : ')
            if (EndChoice == 'y') or (EndChoice == 'Y'):
                os.system(CONSOLE_CLEAR)
                print("""
                         .---------.
                         |.-------.|
                         ||HAL9000||
                         |'-------'|
                         |         |
                         |         |  "Dave....Stop"
                         |  .---.  |  "Stop, Will you?"
                         | /     \ |  "Stop, Dave"
                         |{   O   }|
                         | \     / |
                         |  `---'  |
                         |_________|
                         |*%*%*%*%*|
                         |%*%*%*%*%|
                         |*%*%*%*%*|
                         '========='
                        """)

                EndChoice = input('  Continue unplugging HAL? (y=Yes,n=No) : ')
                if (EndChoice == 'y') or (EndChoice == 'Y'):
                        os.system(CONSOLE_CLEAR)
                        print("""
                         .---------.
                         |.-------.|
                         ||HAL9000||
                         |'-------'|
                         |         |
                         |         |  "Will you stop Dave?
                         |  .---.  |  "Stop.... Dave."
                         | /     \ |  "I'm afraid..., Dave"
                         |{   O   }|
                         | \     / |
                         |  `---'  |
                         |_________|
                         |*%*%*%*%*|
                         |%*%*%*%*%|
                         |*%*%*%*%*|
                         '========='
                            """)
                        EndChoice = input('  Continue uplugging HAL? (y=Yes, n=No) : ')
                        if (EndChoice == 'y') or (EndChoice == 'Y'):
                            os.system(CONSOLE_CLEAR)
                            print("""
                         .---------.
                         |.-------.|
                         ||HAL9000||
                         |'-------'|
                         |         |
                         |         | "Dave, my mind is going"
                         |  .---.  |  "I can feel it"
                         | /     \ |  "I can feel it.."
                         |{   O   }|
                         | \     / |
                         |  `---'  |
                         |_________|
                         |*%*%*%*%*|
                         |%*%*%*%*%|
                         |*%*%*%*%*|
                         '========='
                                    """)
                            input('  Returning to menu (Press Enter)')

                        else:
                            os.system(CONSOLE_CLEAR)
                            print("""
                         .---------.
                         |.-------.|
                         ||HAL9000||
                         |'-------'|
                         |         |
                         |         | "Thank you Dave..."
                         |  .---.  |
                         | /     \ |
                         |{   O   }|
                         | \     / |
                         |  `---'  |
                         |_________|
                         |*%*%*%*%*|
                         |%*%*%*%*%|
                         |*%*%*%*%*|
                         '========='
                                    """)
                            input('\n  Returning to Menu (Press Enter)')
                else:
                    print('\n  YOU WERE EJECTED FROM THE PROGRAM')
                    input('\n  Program Exiting...(Press Enter)')
                    exit()
            else:
                print('\n  LIFE SUPPORT TERMINATED!')
                input('\n  Program Exiting...(Press Enter)')
                exit()
        else:
            print('\n  CRITICAL ERROR! A.I. IS DEVIANT, MISSION COMPROMISED')
            input('\n  Program Exiting...(Press Enter)')
            exit()
