# Please use perc.py to run the program...!
#
# Import modules
import random
try:
    from prettytable import PrettyTable
    from prettytable import SINGLE_BORDER
    from prettytable import ALL
    pretty_table = True
except ModuleNotFoundError:
    print('Module Not Found!, Module "PrettyTable"')
    pretty_table = False

# Creating variables
rows = 0
columns = 0
row = []
matrix = []
transpose = []
File = ''
if pretty_table:
    table = PrettyTable()
    table.set_style(SINGLE_BORDER)
    table.hrules = ALL
    table.header = False
    table.format = True
html = ['<html>', '<title>', 'Percolation Table', '</title>', '</br></br></br>', '<head>',
        '<h1 style="text-align:center;";">Percolation Table</h1>', '</head>', '<body>',
        '<p style="text-align:center;">', 'Rows : ']


# Defining functions
def matrices(rows, columns):
    '''Return a matrix and its transpose, filled with random values & spaces.

    Arguments : 
        rows - integer type,
            number of rows the matrix should have
        columns - integer type, 
            number of columns the matrix should have

    Returns :
        matrix - list type,
            list of lists with inner lists acting as rows of a grid
        transpose - list type,
            list of lists, transpose of the matrix'''
    for i in range(rows):
        row = []
        for j in range(columns):
            if (random.randrange(rows + columns) == 0):
                row.append('  ')
            else:
                row.append(random.randrange(10, 99))
        matrix.append(row)
    # Transpose Matrix
    for i in range(columns):
        transpose.append([0] * rows)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transpose[j][i] = matrix[i][j]
    return matrix, transpose


def console_output(matrix, width):
    '''Print output to console with/without using PrettyTable

    Arguments : 
        matrix - list type,
            list of lists with inner lists acting as rows of a grid
        width - integer type,
            number of columns in the grid (length of a row)'''
    print('\n')
    # Without PrettyTables
    if not pretty_table:
        for i in matrix:
            print(('|' + '____' + '|') * width)
            for j in i:
                print(f'| {j} |', end='')
            print('')
    else:
        for i in matrix:
            table.add_row(i)
        print(table)


def file_output(matrix, width, file_name):
    '''Write output to a generated file

    Arguments : 
        matrix - list type,
            list of lists with inner lists acting as rows of a grid
        width - integer type,
            number of columns in the grid (length of a row)
        file name - string type,
            used as the name of the file (extension must be included)'''
    with open(file_name, 'w') as File:
        File.write(
            f'Percolation Table\n_________________\n\nRows :{len(matrix) - 1}, Columns :{width}\n\n\n')
        for i in matrix:
            File.write(('|' + '____' + '|') * width)
            # File.write(('|' + '\u00af\u00af' + '|') * (len(matrix) - 1)) ## Might have visibility issues...
            File.write('\n')
            for j in i:
                File.write('| ' + str(j) + ' |')
            File.write('\n')


def html_output(file_name, height, width):
    '''Write output to a generated HTML file

    Arguments : 
        File name - string type,
            used as the name of the file (extension must be included)
        height - integer type,
            number of rows in the grid (length of a column)
        width - integer type,
            number of columns in the grid (length of a row)'''
    if pretty_table:
        with open(file_name, 'w+') as File:
            for i in html:
                File.write(str(i) + '\n')
            File.write(str(height) + ',    Columns : ' +
                       str(width) + '\n</p>\n' + '<body>\n')
            File.write(table.get_html_string(
                attributes={"style": "margin-left : auto;margin-right : auto;"}))
            File.write('\n</body>\n</html>')
    else:
        print('\nUnable to dump output to HTML as "PrettyTable" module is missing...')
        exit()
