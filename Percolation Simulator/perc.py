### ### Percolation Table Generator ### ###

# Importing modules
import main as Main
import sys
import datetime

# Creating variables
grid_height = 5
grid_width = 5
data_matrix = []
transpose_matrix = []
perc_list = []
f_name = ''
now = datetime.datetime.now()
time_string = str(now.strftime('%H_%M_%S'))

# Input
# # To validate console arguments
if (len(sys.argv) >= 2):
    try:
        grid_height, grid_width = (sys.argv[1]).split('x')
        grid_height, grid_width = int(grid_height), int(grid_width)
    except ValueError:
        print(
            f'ValueError: Invalid values for argument [height]x[width] "{sys.argv[1]}"')
        exit()
    if (grid_width < 3 or grid_height < 3) or (grid_width > 9 or grid_height > 9):
        print(
            f'OutOfBoundsError: Integer values not in range 3 - 9 "{sys.argv[1]}"')
        exit()

# Process
# # To Create a matrix filled with random values and spaces
# # And the transpose of that matrix
data_matrix, transpose_matrix = Main.matrices(grid_height, grid_width)
# To check whether percolation is possible within a column
for i in transpose_matrix:
    if '  ' in i:
        perc_list.append('NO')
    else:
        perc_list.append('OK')

# # To insert the results in the last row of the grid
data_matrix.append(perc_list)

# Output
# # To Console
Main.console_output(data_matrix, grid_width)
# # To File
f_name += (f'Percolation Table {grid_height}x{grid_width}_{time_string}')
Main.file_output(data_matrix, grid_width, f_name + '.txt')
print(f'\nDumped output to {f_name}.txt file!')
# # To HTML
Main.html_output(f_name + '.html', grid_height, grid_width)
print(f'\nDumped output to {f_name}.html file!')

# # # End Program # # #
