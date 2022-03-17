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
            print("[" + elem + "]", end="")
        print()



def choose_next_number():
    wheighted_number_list = [2, 2, 2, 2, 4, 2, 2, 2, 2, 4]
    num_index = random.randint(0, 9)
    return wheighted_number_list[num_index]



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



def add_new_twos_and_fours(matrix):
    pass



def main():
    matrix = init(get_board_size())
    print_matrix(matrix)




if __name__ == "__main__":
    main()
