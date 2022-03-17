def init(board_size):
    matrix=[]
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append(" ")
        matrix.append(row)
    return matrix

def is_board_full(matrix, return_num_of_empty_spaces=False):
    num_of_empty_spaces = 0
    for row in matrix:
        for elem in row:
            if elem == " ":
                num_of_empty_spaces += 1
    if return_num_of_empty_spaces:
        return num_of_empty_spaces == 0, num_of_empty_spaces
    else:
        return num_of_empty_spaces == 0

matrix = init(3)
is_full = True
num_of_empty_spaces = 0

is_full, num_of_empty_spaces = is_board_full(matrix, True)

print(is_full, " ",  num_of_empty_spaces)
