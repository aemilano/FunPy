# Number System Calculator #

# Made by AMND #

# Variable/Function Definition #

# # print_menu              # Prints Start Menu.
# # number_system_menu      # Prints multiple choices to the user.
# # menu_option             # The Main Menu Option chosen by user.
# # number_system_option    # Number System Menu's option selected by user.
# # in_num                  # Get user input.
# # in_hex                  # Get user input (Hexadecimal).
# # option_select           # Stores the selected option in the number_system_menu()
# # check_invalids          # Check if values exist in number systems to prevent errors.
# # dec_bin                 # Decimal to Binary conversion.
# # bin_dec                 # Binary to Decimal conversion
# # dec_oct                 # Decimal to Octal conversion
# # oct_dec                 # Octal to Decimal conversion
# # dec_hex                 # Decimal to Hexadecimal conversion
# # hex_dec                 # Hexadecimal to Decimal conversion
# # whole                   # Stores the 'whole' half of an number with decimal points (number to the left of decimal point).
# # dec                     # Stores the 'decimal' half of an number with decimal points (numbers to the right of the decimal point).
# # result                  # Result of a conversion.
# # answer                  # Result made ready for output
# # temp                    # Temporary Variable, Used for calculations.
# # places                  # Stores the amount of decimal places of a Number.
# # precision               # Calculation Precision (Set to 8)
# # end_choice              # User's Choice on Process Completion

# Error Code Definition #

# # ErrorCode : UNMATCHED_OPTION        : Program Cannot Match a Listed Option, With The Input Entered
#                                         When Selecting an Option, Make Sure Only the Number Next to the Option is Entered

# # ErrorCode : INVALID_INPUT_TYPE      : Program Cannot Change the Type (str, float, int), of the Input to Whatever Necessary,
#                                         Usually Occurs When the Input Contains a letter, or (In case of Hex Inputs and others) a Symbol

# # ErrorCode : INVALID_VALUE_IN_INPUT  : Occurs When Input Contains a Value (character, number), that Does not Exit in the Number System.
#                                         As an Example, When Converting a Binary Number to Decimal, If the Number Contains a '3', Which Does Not Exist in
#                                         the Binary Number System, the Program Throws This Error to Prevent Crashes.
#                                         Make Note, that When Inputting Hex Numbers, As an Example, Number 10, The Program doesn't Throw this Error
#                                         As Number 1 and 0 Exists in the Hex Number System, However, as Number 10 doesn't, User Must Use the
#                                         Correct Corresponding Hex Value (Hex 'A', for Decimal 10) Instead.

# Changelog #
#    v1.0 - Finished a working, usable program
#    v1.1 - Cleaned up minor bugs and errors, type errors and visual errors
#    v1.2 - More Documentation

# Modules Used #
from decimal import Decimal
import os

# Lists Used #
bin_list = ['0', '1', '.']
oct_list = ['0', '1', '2', '3', '4', '5', '6', '7', '.']
dec_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
            'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f', '.']
num_sys_list = ['Decimal', 'Binary', 'Octal', 'Hexadecimal']

# Initializing Variables
in_num = ''
temp = ''

# Detects Operating System
if (os.name == 'nt'):
    console_clear = 'cls'
else:
    console_clear = 'clear'
# Clears Up Console To De-clutter Console Space(Only Works in a Terminal Such As CMD in Windows)


def clear_console():
    os.system(console_clear)
    return

# Prints Main Menu


def print_menu():
    while True:
        print("""\n
                                 D B O H
                                ^ ^ ^ ^ ^

                         Number System Calculator
                             ****************

                               Version 1.2
                               { A M N D }
    
                    1. Number System Conversion.
    
                    0. Exit Program \n
                                            """)

    # Gets User's Selection and Stores it...
        menu_option = input(' Choose your option : ').strip()
        # Selection Validity Check...
        if (menu_option) != '1' and (menu_option) != '2' and (menu_option) != '0':
            print('\n\a ERROR!! INVALID OPTION SELECTION! PLEASE TRY AGAIN!')
            print(' ErrorCode : UNMATCHED_OPTION')
            input('\n Press Enter to Continue..')
            clear_console()
            continue
        return menu_option


def number_system_menu():
    while True:
        # Print Number System Menu
        print("""\n Number System Conversion.
                       
                   1.  Decimal to Binary
                   2.  Decimal to Octal
                   3.  Decimal to Hexadecimal
                       
                   4.  Binary to Decimal
                   5.  Binary to Octal
                   6.  Binary to Hexadecimal
                       
                   7.  Octal to Decimal
                   8.  Octal to Binary
                   9.  Octal to Hexadecimal
                       
                   10. Hexadecimal to Decimal
                   11. Hexadecimal to Binary
                   12. Hexadecimal to Octal
                       
                   0. Go back to Menu
                       \n""")
        # Get User Option
        number_system_option = input(' Choose your option : ').strip()
        # Selection Validity Check
        try:
            number_system_option = int(number_system_option)
        except ValueError:
            print('\n\a ERROR!! INVALID OPTION SELECTION! PLEASE TRY AGAIN!')
            print(' {ErrorCode : UNMATCHED_OPTION}')
            input('\n Press Enter to Continue..')
            clear_console()
            continue
        if (number_system_option) < 0 or (number_system_option) > 12:
            print('\n\a ERROR!! INVALID OPTION SELECTION! PLEASE TRY AGAIN!')
            print(' {ErrorCode : UNMATCHED_OPTION}')
            input('\n Press Enter to Continue..')
            clear_console()
            continue
        return number_system_option

# Get User Input


def input_num(sys_name):
    global in_num
    in_num = input('\n Enter the {} number to be converted : '.format(
        num_sys_list[sys_name])).strip()
    # Input validity Check
    while True:
        try:
            in_num = int(in_num)
        except ValueError:
            try:
                in_num = Decimal(in_num)
            except:
                print('\n\a ERROR!! INVALID INPUT! PLEASE CHECK THE NUMBER!')
                print(' {ErrorCode : INVALID_INPUT_TYPE}')
                input('\n Press Enter to Continue..')
                return True
        break

# Get User Input (Hex)


def input_hex():
    global in_num
    in_num = input('\n Enter the Hexadecimal number to be converted : ')
    return


def check_invalids(num, numlist):
    # Check Validity of the Input Number
    for i in str(num):
        # Check if Each Digit is Valid
        if i not in numlist:
            # If False, Show Errors and Return to Menu
            print(
                '\n\a ERROR!! \n ONE OR MORE DIGITS/CHARACTERS DOES NOT EXIST IN INPUT NUMBER SYSTEM!')
            print(' Conflicting character(s)/digit(s) : ', i)
            print(' {ErrorCode : INVALID_VALUE_IN_INPUT}')
            input('\n Press Enter to Continue..')
            return True
    # If All Digits are Valid, Continue
    return False


def dec_bin():
    global in_num
    # Check Input Validity
    if (check_invalids(in_num, dec_list)):
        return True
    # Check if Input is Integer or Decimal
    if ('.' not in str(in_num)):
        # Check if Input == 0, and if so, Set the Output to Zero
        # To Avoid Output Errors
        if (in_num == 0) or (in_num == '0'):
            result = '0'
        else:
            result = str(bin(int(in_num)).lstrip('0b'))
    else:
        # Check if Input == 0
        # Separate Number at Decimal Point
        whole, dec = str(in_num).split('.')
        # Convert Split Number to Integers
        whole = int(whole)
        dec = int(dec)
        # Convert 'Whole' Part of the Number
        # Check if 'Whole' Part is 0, in Case of a Fractional Number Input
        if (whole == 0):
            # Set Whole Part to 0 for Cleaned and Visually Better Output
            result = '0'+'.'
        else:
            result = bin(whole).lstrip('0b') + '.'
        # Get Number of Decimal Places
        places = len(str(dec))
        # Converts dec to It's Decimal Format
        dec = dec / (10 ** places)
        precision = 20
        while True:
            # If dec X 2 > 1, Write 1
            dec *= 2
            if (dec >= 1):
                result += '1'
                dec -= 1
            else:
                result += '0'
            # Check If dec Value is Empty to Stop Loop
            if (dec == 0):
                break
            # Set Max Number of Decimal Points in Case of Indivisible Numbers
            precision -= 1
            if (precision <= 0):
                result += '+'
                break
    # Print Result
    return result


def bin_dec():
    global in_num
    answer = ''
    # Check Input Validity
    if (check_invalids(in_num, bin_list)):
        return True
    # Check if Input is Integer or Decimal
    if ('.' not in str(in_num)):
        # Check if Input == 0, and if so, Set the Output to Zero
        # To Avoid Output Errors
        if (in_num == 0) or (in_num == '0'):
            answer = '0'
        else:
            answer = str(int(str(in_num), 2))
    else:
        # Separate Number at Decimal Point
        whole, dec = str(in_num).split('.')
        # Convert Whole number to Decimal
        # Check if 'Whole' Part is 0, in Case of a Fractional Number Input
        if (whole == ''):
            # Set Whole Part to 0 for Cleaned and Visually Better Output
            whole = '0'
        else:
            whole = int(whole, 2)
        # Count Decimal Places to the Right of the Decimal Point
        places = len(dec)
        temp = 0
        # Get Numbers at Each Decimal Place and Add Them Together.
        for i in range(places):
            # Used Formula : (1/(2 to the Power of (each Iteration+1))*(Value At Decimal Places)
            # Where temp is the Number of Decimal Places and i is the Iteration.
            temp += (1 / (2 ** (i + 1))) * int(dec[i])
        answer = int(whole)+(temp)
    return answer


def dec_oct():
    global in_num
    answer = ''
    # Check Input Validity
    if (check_invalids(in_num, dec_list)):
        return True
    # Check if Input is Integer or Decimal
    if ('.' not in str(in_num)):
        # Check if Input == 0, and if so, Set the Output to Zero
        # To Avoid Output Errors
        if (in_num == 0) or (in_num == '0'):
            answer = '0'
        else:
            # Use oct() to Convert the Whole Number to Octal
            answer = str(oct(int(in_num)).lstrip('0o'))
    else:
        # Separate Number at Decimal Point
        whole, dec = str(in_num).split('.')
        # Check if 'Whole' Part is 0, in Case of a Fractional Number Input
        if (whole == '') or (whole == '0'):
            # Set Whole Part to 0 for Cleaned and Visually Better Output
            result = '0'
        else:    
            # Convert Whole Number to Octal
            result = oct(int(whole)).lstrip('0o')
        dec = int(dec)
        # Get the Amount of Decimal Places
        places = len(str(dec))
        # Convert the Number to a Decimal Value
        dec = (dec / (10 ** places))
        # Set Calculation Precision
        precision = 20
        temp = ''
        while True:
            # Used Formula : Multiplies Decimal Value by 8, When a Integral Appears, 
            # Add it to the result, Else, Write Zero.
            dec *= 8
            # Check if an Integral is Present
            if (dec >= 1):
                # Separate Number at Decimal Point
                whole, dec = str(dec).split('.')
                # Add Integral to temp
                temp += whole
                # Get the Amount of Decimal Places in Dec
                places = len(str(dec))
                # Convert Dec to A Decimal Value
                dec = (int(dec) / 10 ** places)
            elif (dec < 1) and (dec != 0):
                # Write 0 to temp
                temp += '0'
            # If No More Decimals are Present, End Loop
            if (dec == 0):
                break
            precision -= 1
            # If Precision Limit Reach, Exit Loop, Indicate the Number Keeps Going..
            if (precision <= 0):
                temp += '+'
                break
        answer = str(result+'.'+str(temp))
    return answer


def oct_dec():
    global in_num
    answer = ''
    # Check Input Validity
    if (check_invalids(in_num, oct_list)):
        return True
    # Check if Input is Integer or Decimal
    if ('.' not in str(in_num)):
        # Check if Input == 0, and if so, Set the Output to Zero
        # To Avoid Output Errors
        if (in_num == 0) or (in_num == '0'):
            answer = '0'
        else:
            # Use int() to Convert the Whole Number to Decimal
            answer = str(int(str(in_num), 8))
    else:
        # Separate Number at Decimal Point
        whole, dec = str(in_num).split('.')
        # Check if 'Whole' Part is 0, in Case of a Fractional Number Input
        if (whole == ''):
            # Set Whole Part to 0 for Cleaned and Visually Better Output
            whole = 0
        else:    
            # Convert Whole Number to Decimal
            whole = str(int(whole, 8))
        # Get Amount of Decimal Places
        places = len(dec)
        # Get Numbers from Each Decimal Place and Add them Together
        temp = 0
        for i in range(places):
            # Used Formula : (1 / 8(to the Power of Each Iteration+1) * by Value at Each Decimal Place)
            # Where i = the Iteration, dec = Decimal Value
            temp += (1 / (8 ** (i + 1))) * int(dec[i])
        answer = str(int(whole) + temp)
    return answer


def dec_hex():
    global in_num
    answer = ''
    # Check Input Validity
    if (check_invalids(in_num, dec_list)):
        return True
    # Check if Input is Integer or Decimal
    if ('.' not in str(in_num)):
        # Check if Input == 0, and if so, Set the Output to Zero
        # To Avoid Output Errors
        if (in_num == 0) or (in_num == '0'):
            answer = '0'
        else:
            # Use hex() to Convert the Whole Number to Hexadecimal
            answer = str(hex(int(in_num)).lstrip('0x')).upper()
    else:
        # Separate Number at Decimal Point
        whole, dec = str(in_num).split('.')
        # Check if 'Whole' Part is 0, in Case of a Fractional Number Input
        if (whole == '0') or (whole == ''):
            # Set Whole Part to 0 for Cleaned and Visually Better Output
            result = '0'+'.'
        else:
            # Convert Whole Number to Decimal
            result = (hex(int(whole)).lstrip('0x')).upper()+'.'
        # Get Amount of Decimal Places
        places = len(str(dec))
        # Convert Number to a Decimal
        dec = int(dec) / (10 ** places)
        # Set Precision
        precision = 20
        temp = ''
        while True:
            # Formula Used : Multiply by 16, 
            # If Integral is Present Add it to the Result, Else Write Zero
            dec *= 16
            # Check if an Integral is Present
            if (dec >= 1):
                # Separate Number at Decimal Point
                whole, dec = str(dec).split('.')
                # Convert Integral to Hexadecimal
                temp += (hex(int(whole))).lstrip('0x')
                # Get Amount of Decimal Points
                places = len(str(dec))
                # Convert Back to a Decimal Value
                dec = int(dec) / (10 ** places)
            elif (dec < 1) and (dec != 0):
                # Write 0 to temp
                temp += '0'
            if (dec == 0):
                # If No Decimals are Present, End Loop
                break
            precision -= 1
            if (precision <= 0):
                temp += '+'
                break
        answer = str(result+(temp).upper())
    return answer


def hex_dec():
    global in_num
    answer = ''
    # Check Input Validity
    if (check_invalids(in_num, hex_list)):
        return True
    # Check if Input is Integer or Decimal
    if ('.' not in str(in_num)):
        # Check if Input == 0, and if so, Set the Output to Zero
        # To Avoid Output Errors
        if (in_num == 0) or (in_num == '0'):
            answer = '0'
        else:
            # Convert the Integer to Hex Directly
            answer = str(int(in_num, 16))
    else:
        # Separate Number At Decimal Point
        whole, dec = str(in_num).split('.')
        # Check if 'Whole' Part is 0, in Case of a Fractional Number Input
        if (whole == 0) or (whole == ''):
            # Set Whole Part to 0 for Cleaned and Visually Better Output
            result = '0'+'.'
        else:
            # Convert Whole Part of the Number Directly
            result = str(int(whole, 16))+'.'
        # Get Amount of Decimal Places
        places = len(str(dec))
        temp = 0
        for i in range(places):
            # Formula Used : 
            # (1 / 16 (to the Power of Iteration + 1)) * (Value at Each Decimal Place Converted to Hexadecimal)
            temp += (1 / (16 ** (i + 1))) * int(dec[i], 16)
        answer = str(float(result)+temp)
    return answer


# Driver Code
while True:
    # Show Menu
    clear_console()
    temp2 = print_menu()
    # If Option 1 is Selected
    if (temp2 == '1'):
        while True:
            clear_console()
            # Show Number System Menu
            option_select = (number_system_menu())
            # If Option 1 is Selected
            if (option_select == 1):
                # Get Input
                if (input_num(0) == True):
                    continue
                # Calculate Conversion and Show Output
                result = dec_bin()
                # If Error Occurs, Halt and Go back to num-sys-menu
                if (result == True):
                    continue
                print('\n Result : ', result, '(Binary)')
            # If Option 2 is Selected
            if (option_select == 2):
                # Get Input
                if (input_num(0) == True):
                    continue
                # Calculate Conversion and Show Output
                result = dec_oct()
                # If Error Occurs, Halt and Go back to num-sys-menu
                if (result == True):
                    continue
                print('\n Result : ', result, '(Octal)')
            # If Option 3 is Selected
            if (option_select == 3):
                # Get Input
                if (input_num(0) == True):
                    continue
                # Calculate Conversion and Show Output
                result = dec_hex()
                # If Error Occurs, Halt and Go back to num-sys-menu
                if (result == True):
                    continue
                print('\n Result : ', result, '(Hexadecimal)')
            # If Option 4 is Selected
            if (option_select == 4):
                # Get Input
                if (input_num(1) == True):
                    continue
                # Calculate Conversion and Show Output
                result = bin_dec()
                # If Error Occurs, Halt and Go back to num-sys-menu
                if (result == True):
                    continue
                print('\n Result : ', result, '(Decimal)')
            # If Option 5 is Selected
            if (option_select == 5):
                # Get Input
                if (input_num(1) == True):
                    continue
                # Calculate Conversion and Show Output
                in_num = bin_dec()
                # If Error Occurs, Halt and Go back to num-sys-menu
                if (in_num == True):
                    continue
                result = dec_oct()
                print('\n Result : ', result, '(Octal)')
            # If Option 6 is Selected
            if (option_select == 6):
                # Get Input
                if (input_num(1) == True):
                    continue
                # Calculate Conversion and Show Output
                in_num = bin_dec()
                # If Error Occurs, Halt and Go back to num-sys-menu
                if (in_num == True):
                    continue
                result = dec_hex()
                print('\n Result : ', result, '(Hexadecimal)')
            # If Option 7 is Selected
            if (option_select == 7):
                # Get Input
                if (input_num(2) == True):
                    continue
                # Calculate Conversion and Show Output
                result = oct_dec()
                # If Error Occurs, Halt and Go back to num-sys-menu
                if (result == True):
                    continue
                print('\n Result : ', result, '(Decimal)')
            # If Option 8 is Selected
            if (option_select == 8):
                # Get Input
                if (input_num(2) == True):
                    continue
                # Calculate Conversion and Show Output
                in_num = oct_dec()
                # If Error Occurs, Halt and Go back to num-sys-menu
                if (in_num == True):
                    continue
                result = dec_bin()
                print('\n Result : ', result, '(Binary)')
            # If Option 9 is Selected
            if (option_select == 9):
                # Get Input
                if (input_num(2) == True):
                    continue
                # Calculate Conversion and Show Output
                in_num = oct_dec()
                # If Error Occurs, Halt and Go back to num-sys-menu
                if (in_num == True):
                    continue
                result = dec_hex()
                print('\n Result : ', result, '(Hexadecimal)')
            # If Option 10 is Selected
            if (option_select == 10):
                # Get Input
                input_hex()
                # Calculate Conversion and Show Output
                result = hex_dec()
                # If Error Occurs, Halt and Go back to num-sys-menu
                if (result == True):
                    continue
                print('\n Result : ', result, '(Decimal)')
            # If Option 11 is Selected
            if (option_select == 11):
                # Get Input
                input_hex()
                # Calculate Conversion and Show Output
                in_num = hex_dec()
                # If Error Occurs, Halt and Go back to num-sys-menu
                if (in_num == True):
                    continue
                result = dec_bin()
                print('\n Result : ', result, '(Binary)')
            # If Option 12 is Selected
            if (option_select == 12):
                # Get Input
                input_hex()
                # Calculate Conversion and Show Output
                in_num = hex_dec()
                # If Error Occurs, Halt and Go back to num-sys-menu
                if (in_num == True):
                    continue
                result = dec_oct()
                print('\n Result : ', result, '(Octal)')
            # If Option 13 is Selected
            if (option_select == 0):
                break
            else:
                # Process Completion
                print('\n Process Complete!')
                print('\n Input "Enter" for New Attempt')
                print(' "X" for Main Menu')
                print(' "N" to Exit Program')
                end_choice = input('\n Choose an Option : ').strip()
                # If User Wants to Retry
                if (end_choice == ''):
                    continue
                # If User Wants to Exit Program
                elif (end_choice == 'n') or (end_choice == 'N'):
                    print('\n Program Exited...')
                    exit()
                # If User Wants to Go to Main Menu
                elif (end_choice == 'X') or (end_choice == 'x'):
                    break
                # Invalid Input, Default to Main Menu
                else:
                    break
    # If Option 2 (Exit) was Chosen, Prompt Confirmation and Exit
    if (temp2 == '0'):
        # Prompt Confirmation
        end_choice = input(
            '\n Are you sure you want to exit program? (y = Yes, n = No)')
        # Exit Program
        if (end_choice == 'y') or (end_choice == 'Y'):
            print('\n Program Exited..')
            exit()
        # Go Back to Menu 
        elif (end_choice == 'n') or (end_choice == 'N'):
            continue
        # Invalid Choice, Go Back to Menu
        else:
            continue
    continue