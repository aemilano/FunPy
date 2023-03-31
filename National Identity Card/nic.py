# nic.py
# Coded by AMND
# Parses through an NIC to get the details of the card holder

# Importing modules
from datetime import datetime
import os

# Initializing Variables
nic_card = ''
nic_version = ''
voting_eligibility = ''
numbers = 0
letter = ''
birth_year = ''
birth_m_d = ''
end = ''
gender = ''
validity = ''

# Clear console
console_clear = 'cls' if os.name == ('nt') else 'clear'


def print_menu():
    "prints main menu"
    print("""
                         *******************
                             N I C _ P Y
                           ***************
                               A M N D

        ~ Use the National Identity Card number,
                            to get details about the card holder ~
    \n\n""")

# Input
# Get NIC number from user


def get_input():
    "Gets and returns users input"
    return (input('\n Enter your N.I.C. Number : ').upper()).strip(' ')

# Process


def check_validity(nic_card):
    "Checks if NIC number is valid, returns version"
    if (len(nic_card) == 10):
        if (nic_card[-1] == 'V') or (nic_card[-1] == 'X'):
            return 'Old'
        else:
            print_error()
            return False
    elif (len(nic_card) == 12):
        try:
            nic_card = int(nic_card)
        except ValueError:
            print_error()
            return False
        return 'New'
    else:
        print_error()
        return False


def old_split_string(nic_card):
    "Splits card number and returns the numbers, final letter"
    return nic_card[:9], nic_card[-1]


def old_get_byear(numbers):
    "Returns last two numbers of card holders birth year on a old card"
    return numbers[:2]


def old_gen_birth(numbers):
    "Returns holders gender and birth month, day on a old card"
    if (int(numbers[2:5]) > 500):
        gender = 'Female'
        numbers = str(int(numbers[2:5]) - 501)
    else:
        gender = 'Male'
        numbers = str(int(numbers[2:5]) - 1)
    try:
        numbers = datetime.strptime(numbers, "%j")
        numbers = numbers.strftime("%B"), numbers.strftime("%d")
    except ValueError:
        print_error()
        return gender, False
    return gender, numbers


def new_byear(numbers):
    "Returns the card holders birth year on a new card"
    return numbers[:4]


def new_gen_birth(numbers):
    "Returns the card holders gender and birth month, day on a new card"
    if (int(numbers[4:7]) > 500):
        gender = 'Female'
        # Subtract extra 1 from the birth values since count starts at 0 (Jan 1st = 0, Jan 2nd = 1 etc.)
        numbers = str(int(numbers[4:7]) - 501)
    else:
        gender = 'Male'
        numbers = str(int(numbers[4:7]) - 1)
    try:
        numbers = datetime.strptime(numbers, "%j")
        numbers = numbers.strftime("%B"), numbers.strftime("%d")
    except ValueError:
        print_error()
        return gender, False
    return gender, numbers


def eligible_vote(letter):
    if (letter == 'V'):
        return 'Eligible'
    else:
        return 'Not Eligible'


def print_error():
    print('\n ERROR!! INVALID NIC!')
    input(' Press Enter to Re-attempt...')

# Driver Code
while (end == ''):
    # Clear Console
    os.system(console_clear)
    print_menu()
    nic_card = get_input()
    # Check whether the NIC is valid
    validity = check_validity(nic_card)
    if not (validity):
        continue
    elif (validity == 'Old'):
        # Break NIC to two variables, one for numbers and the other for final letter
        numbers, letter = old_split_string(nic_card)
        # Check if numbers are all integers
        try:
            numbers = str(int(numbers))
        except ValueError:
            print_error()
            continue
        birth_year = '19'+str(old_get_byear(numbers))
        gender, birth_m_d = old_gen_birth(numbers)
        # If a date calculation error occurs, throw error
        if not birth_m_d:
            continue
        voting_eligibility = eligible_vote(letter)
    elif (validity == 'New'):
        birth_year = new_byear(nic_card)
        gender, birth_m_d = new_gen_birth(nic_card)
        if not birth_m_d:
            continue

    # Output
    print('\n Card Version        : ', validity)
    print(' Birthday            : ', birth_year, birth_m_d[0], birth_m_d[1])
    print(' Gender              : ', gender)
    if (validity == 'Old'):
        print(' Voting Eligibility  : ', voting_eligibility)
    end = input(
        '\n Program Complete! , Press Enter to Re-Attempt or "n" to Quit...')
