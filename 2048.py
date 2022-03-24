import random



def init(board_size):
    matrix=[]
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append(" ")
        matrix.append(row)
    return matrix



def get_board_size():
    return int(input("mekkora legyen a tábla?"))
    


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
        for i in range(num_of_valid_spaces - 1):
            coords = choose_random_coordinates(len(matrix)-1)
            while not is_position_free(matrix, coords):
                coords = choose_random_coordinates(len(matrix))
            matrix[coords[0]][coords[1]] = choose_next_number()
    return matrix
            



def main():
    matrix = init(get_board_size())
    print_matrix(matrix)
    matrix = add_new_twos_and_fours(matrix)
    print("\n")
    print_matrix(matrix)


if __name__ == "__main__":
    main()
