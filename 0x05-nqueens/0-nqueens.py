#!/usr/bin/python3
"""
Solving N-Queens problem using backtracking
"""


def is_safe(board, row, col):
    """
    Checks if the current queen can be placed safely in the board
    :param board: (list of lists)
    :param row: (int) the row to place the queen
    :param col: (int) the column to place the queen
    :return: (bool) True if the queen can be placed, False otherwise
    """
    for i in range(row):
        if board[i][1] == col or abs(board[i][0] - row) == abs(
                board[i][1] - col):
            return False
    return True


def solve_util(board, row, n, res):
    """Solving the N-queen recursively """
    if row == n:
        res.append([[r, c] for r, c in board])
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = [row, col]
            solve_util(board, row + 1, n, res)
            board[row] = [-1, -1]


def solve_n_queens(n):
    """Printing solution of N-Queen problem"""
    board = [[-1, -1] for _ in range(n)]
    res = []
    solve_util(board, 0, n, res)
    for solution in res:
        print(solution)


if __name__ == "__main__":
    import sys

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except IndexError:
        print("Usage: nqueens N")
        sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(n)
