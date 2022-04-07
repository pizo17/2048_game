import random
import sys



def init(matrix, board_size):
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append(" ")
        matrix.append(row)



def get_board_size():
    return int(input("mekkora legyen a tábla? "))
    


def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(f"[{elem}]", end="")
        print()



def choose_next_number():
    wheighted_number_list = [2, 2, 2, 2, 4, 2, 2, 2, 2, 4]
    num_index = random.randint(0, 9)
    return wheighted_number_list[num_index]



def choose_random_coordinates(size):
    coords = []
    for i in range(2):
        coords.append(random.randint(0, size))
    return coords



def is_position_free(matrix, coords):
    return matrix[coords[0]][coords[1]] == " "



def is_board_full(matrix, return_num_of_empty_spaces=False):
    num_of_valid_spaces = 0
    for row in matrix:
        for elem in row:
            if elem == " " and num_of_valid_spaces <= 2:
                num_of_valid_spaces += 1
    if return_num_of_empty_spaces:
        return num_of_valid_spaces == 0, num_of_valid_spaces
    else:
        return num_of_valid_spaces == 0



def add_new_twos_and_fours(matrix):
    is_full, num_of_valid_spaces = is_board_full(matrix, True)
    if not is_full:
        for i in range(1, num_of_valid_spaces):
            coords = choose_random_coordinates(len(matrix)-1)
            while not is_position_free(matrix, coords):
                coords = choose_random_coordinates(len(matrix)-1)
            matrix[coords[0]][coords[1]] = choose_next_number()
            


def user_character_input():
    return input()



def move_up(matrix):
    for i in range(1, len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i-1][j] == " " and matrix[i][j] != " ":
                matrix[i-1][j] = matrix[i][j]
                matrix[i][j] = " "



def move_down(matrix):
    for i in reversed(range(len(matrix)-1)):
        for j in range(len(matrix[i])):
            if matrix[i+1][j] == " " and matrix[i][j] != " ":
                matrix[i+1][j] = matrix[i][j]
                matrix[i][j] = " "



def move_left(matrix):
    for i in range(len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[i][j-1] == " " and matrix[i][j] != " ":
                matrix[i][j-1] = matrix[i][j]
                matrix[i][j] = " "



def move_right(matrix):
    for i in range(len(matrix)):
        for j in reversed(range(len(matrix[i])-1)):
            if matrix[i][j+1] == " " and matrix[i][j] != " ":
                matrix[i][j+1] = matrix[i][j]
                matrix[i][j] = " "



def one_cell_move(usr_input, matrix):
    if usr_input == "w":
        move_up(matrix)
    if usr_input == "a":
        move_left(matrix)
    if usr_input == "s":
        move_down(matrix)
    if usr_input == "d":
        move_right(matrix)



def add_up(matrix):
    j_start = 0
    for i in range(len(matrix)-1):
        for j in range(j_start, len(matrix[i])):
            if matrix[i][j] == " ":
                j_start += 1
            elif matrix[i][j] == matrix[i+1][j]:
                matrix[i][j] += matrix[i+1][j]
                matrix[i+1][j] = " "
                j_start += 1



def add_down(matrix):
    j_start = 0
    for i in reversed(range(len(matrix)-1)):
        for j in range(j_start, len(matrix[i])):
            if matrix[i][j] == " ":
                j_start += 1
            elif matrix[i][j] == matrix[i+1][j]:
                matrix[i+1][j] += matrix[i][j]
                matrix[i][j] = " "
                j_start += 1
            


def add_left(matrix):
    i_start = 0
    for j in range(1, len(matrix[1])):
        for i in range(i_start, len(matrix)):   
            if matrix[i][j] == " ":
                i_start += 1
            elif matrix[i][j] == matrix[i][j-1]:
                matrix[i][j-1] += matrix[i][j]
                matrix[i][j] = " "
                i_start += 1



def add_right(matrix):
    i_start = 0
    for j in reversed(range(len(matrix[1])-1)):
        for i in range(i_start, len(matrix)):
            if matrix[i][j] == " ":
                i_start += 1
            elif matrix[i][j] == matrix[i][j+1]:
                matrix[i][j+1] += matrix[i][j]
                matrix[i][j] = " "
                i_start += 1



def add(matrix, usr_input):
    if usr_input == "w":
        add_up(matrix)
    if usr_input == "a":
        add_left(matrix)
    if usr_input == "s":
        add_down(matrix)
    if usr_input == "d":
        add_right(matrix)



def main():
    matrix = []
    init(matrix, get_board_size())
    user_dir = ""
    add_new_twos_and_fours(matrix)
    print("\n")
    print_matrix(matrix)
    while(True):
        user_dir = user_character_input()
        add(matrix, user_dir)
        one_cell_move(user_dir, matrix)
        add_new_twos_and_fours(matrix)
        print("\n")
        print_matrix(matrix)



if __name__ == "__main__":
    main()
