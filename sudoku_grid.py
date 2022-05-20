def row_correct(sudoku : list, row_no : int):
    numbers_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for number in numbers_to_check:
        if (sudoku[row_no].count(number)) > 1:
            return False
    return True

def column_correct(sudoku : list, column_no : int):
    numbers_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    current_column = []
    for row in sudoku:
        current_column.append(row[column_no])
    for number in numbers_to_check:
        if current_column.count(number) > 1:
            return False
    return True

def block_correct(sudoku : list, row_no : int, column_no : int):
    numbers_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    current_column = []
    index_one = 0
    while (index_one + row_no) < len(sudoku) and index_one < 3:
        index_two = 0
        while (index_two + column_no) < len(sudoku) and index_two < 3:
            current_column.append(sudoku[row_no + index_one][column_no + index_two])
            index_two += 1
        index_one += 1
    for numbers in numbers_to_check:
        if current_column.count(numbers) > 1:
            return False
    return True

def sudoku_grid_correct(sudoku : list):
    for row in range(len(sudoku)):
        if row_correct(sudoku, row) == False:
            return False
    for column in range(len(sudoku)):
        if column_correct(sudoku, column) == False:
            return False
    if block_correct(sudoku, 0, 0) == False:
        return False
    if block_correct(sudoku, 0, 3) == False:
        return False
    if block_correct(sudoku, 0, 6) == False:
        return False
    if block_correct(sudoku, 3, 0) == False:
        return False
    if block_correct(sudoku, 3, 3) == False:
        return False
    if block_correct(sudoku, 3, 6) == False:
        return False
    if block_correct(sudoku, 6, 0) == False:
        return False
    if block_correct(sudoku, 6, 3) == False:
        return False
    if block_correct(sudoku, 6, 6) == False:
        return False
    return True

if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    print(sudoku_grid_correct(sudoku2))