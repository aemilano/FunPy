# Import modules
import random

# Create variables
secret_number = []
guess_number = 0
attempt_num = 0
guess = 0
result = ['X', 'X', 'X', 'X']
guessed_list = []
replay = ''

def menu():
    print('''
            Hi, Welcome to GameInt
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Number to Guess : XXXX
                                Color Mapping :
                                    1 - White,  2 - Blue,  3 - Red
                                    4 - Yellow, 5 - Green, 6 - Purples\n''')
def top_tab():
    print(''' 
\t\t\t\tAttempt Number\t\tGuess\t\t Result\n
    ''')

def gen_secret():
    num = []
    for i in range(4):
        num.append(random.randrange(1, 7))
    return num


def mark(guessed_list, secret_number):
    for i in range(len(guessed_list)):
        if guessed_list[i] in secret_number:
            if guessed_list[i] == secret_number[i]:
                result[i] = 1
            else:
                result[i] = 0
    return result


def check_input(guess_number):
    if guess_number == '0000':
        exit()
    if not (len(guess_number) == 4):
        print('Error : Number should be 4 digits in length')
        return False
    for i in guess_number:
        if int(i) > 6 or int(i) < 1:
            print('Error : All digits in number, should be within range 1 - 6')
            return False
    return True


while True:
    menu()
    top_tab()
    secret_number = gen_secret()
    for i in range(1, 9):
        guessed_list = []
        result = ['X', 'X', 'X', 'X']
        # Input
        while True:
            guess_number = input('\nEnter your guess : ')
            if not check_input(guess_number):
                continue
            else:
                break
        #Process
        for j in guess_number:
            guessed_list.append(int(j))
        result = mark(guessed_list, secret_number)
        print(f'\t\t\t\t{i}\t\t\t{guess_number}\t\t',*result , sep =' ')
        # Output
        if (result[0] == 1 and result[1] == 1 and result[2] == 1 and result[3] == 1):
            print(f'\nCongratulations! You Won!\nYou scored {110 - (i * 10)} Points!')
            break
        elif i == 8:
            print('\nThe number was : ', *secret_number, sep = '')
    print('\nDo you want to play another game? (Y/n)')
    replay = input('Enter an option : ')
    if (replay == 'y'):
        continue
    else:
        exit()
