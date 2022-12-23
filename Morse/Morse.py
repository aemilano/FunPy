# Morse Code encoder/decoder
# Console Args Required
#   # input file(text)
#   # output file(text)
#   # flag (-e {encode} / -d {decode})
#
#  Ex. Q1.py input.txt output.txt -e

# Creating Variables
import sys
file_name = 0
output_file = 0
operation = ''
letter = ''
text = []
data = ''
CIPHER = {
    'A': '.-',   'N': '-.',   '1': '.----',
    'B': '-...', 'O': '---',  '2': '..---',
    'C': '-.-.', 'P': '.--.', '3': '...--',
    'D': '-..',  'Q': '--.-', '4': '....-',
    'E': '.',    'R': '.-.',  '5': '.....',
    'F': '..-.', 'S': '...',  '6': '-....',
    'G': '--.',  'T': '-',    '7': '--...',
    'H': '....', 'U': '..-',  '8': '---..',
    'I': '..',   'V': '...-', '9': '----.',
    'J': '.---', 'W': '.--',  '0': '-----',
    'K': '-.-',  'X': '-..-',
    'L': '.-..', 'Y': '-.--',
    'M': '--',   'Z': '--..',
}


# Import Modules

# Function

def get_key(val) -> str:
    """ Get key by its corresponding value in the dictionary

    Parameters :
        val -> str
    Returns :
        key -> str
    """
    for key, value in CIPHER.items():
        if value == val:
            return key


# Get Inputs
file_name = sys.argv[1]
output_file = sys.argv[2]
operation = sys.argv[3]

# Process
with open(file_name, 'r') as File:
    text = File.read()
    text = text.upper()

# Output
if operation == '-e':
    for i in text:
        if i in CIPHER:
            data += CIPHER[i] + ' '
        elif i == ' ':
            data += '   '
    with open(output_file, 'w') as File:
        File.write(data)
elif operation == '-d':
    for i in text:
        if i == ' ' and letter != '':
            data += get_key(letter) + ' '
            letter = ''
        elif i == ' ' and letter == '':
            data += ' '
        else:
            letter += i
    with open(output_file, 'w') as File:
        File.write(data)
