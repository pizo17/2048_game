def init(board_size):
    matrix=[]
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append("["+" "+"]")
        matrix.append(row)
    return matrix



def get_board_size():
    return int(input("mekkora legyen a tábla?"))
    


def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end="")
        print()



def add_number(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1



def main():
    matrix = init(get_board_size())
    print_matrix(matrix)




if __name__ == "__main__":
    main()
