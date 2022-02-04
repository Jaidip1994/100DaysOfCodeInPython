# board = [
#     ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
#     ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
#     ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
#     ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
#     ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
#     ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
#     ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
#     ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
#     ['.', '.', '.', '.', '8', '.', '.', '7', '9']
# ]

# Problem Description: https://leetcode.com/problems/valid-sudoku/submissions/

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]


def checkInRow(board):
    for i in range(9):
        exist = set()
        for j in range(9):
            if '.' == board[i][j]:
                continue

            if board[i][j] in exist:
                return True

            exist.add(board[i][j])
        # print(exist)
    return False

def checkInColumn(board):
    for i in range(9):
        exist = set()
        for j in range(9):
            if '.' == board[j][i]:
                continue
            if board[j][i] in exist:
                return True
            exist.add(board[j][i])
        # print(exist)
    return False

def notInBox(arr, startRow, startCol):
    st = set()
    # print(startRow, startCol)
    for row in range(0,3):
        for col in range(0,3):
            curr = arr[row + startRow][col + startCol]
            if curr in st:
                return True
            if curr != '.':
                st.add(curr)
    return False

def checkForEachGrid(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if notInBox(board, i - i % 3, j - j % 3):
                return True
    return False

print(not (checkInRow(board) or checkInColumn(board) or checkForEachGrid(board)))