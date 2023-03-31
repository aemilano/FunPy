# Import modules
import sys
import random

# Creating Variables
enc_file = 0
dec_file = 0
data = ''
data_output = ''
line_size = 0

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         ' ', ',', '.', '"', '(', ')', '!', '&', '-', '*', '?', ';', ':',
         '/', '_', '@', '#', "'", '\n', '0', '1', '2', '3', '4', '5', '6',
         '7', '8', '9', '$', '%', '^', '+', '=', '\\', '|', '~', '`', '<',
         '>', '{', '}', '[', ']']

alpha_code = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13',
             '14','15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
             '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
             '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52',
             '00', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64',
             '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77',
             '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90',
             '91', '92', '93', '94', '95']

# Open clear text file and store data
with open(sys.argv[2], 'r') as enc_file:
    data = enc_file.read()
# Get Key
if len(sys.argv) == 5:
    seed = sys.argv[4].strip(' ')
    random.seed(seed)
    random.shuffle(alpha_code)

# Encrypt data
if sys.argv[1] == '-e':
    for i in data:
        if i in alpha:
            data_output += alpha_code[alpha.index(i)] + ' '
        else:
            data_output += i + ' '
    # Output data to file
    with open(sys.argv[3], 'w') as dec_file:
        dec_file.write(data_output)
        print('\nEncryption Complete!')

# Decrypt data
elif sys.argv[1] == '-d':
    data = data.split(' ')
    for i in data:
        if i in alpha_code:
            data_output += alpha[alpha_code.index(i)]
    with open(sys.argv[3], 'w') as dec_file:
        dec_file.write(data_output)
        print('\nDecryption Complete!')