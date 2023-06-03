def is_safe(row, col, board):
    # Check the column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check the diagonal (upper left)
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check the diagonal (upper right)
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(n):
    solutions = []  # List to store all valid solutions
    board = [['.' for _ in range(n)] for _ in range(n)]  # Initialize an empty chessboard

    # Start the recursive backtracking
    find_board(n, solutions, board, 0)

    return solutions

def find_board(n, solutions, board, row):
    if row == n:
        # All queens have been placed successfully, construct a solution
        solution = []
        for r in board:
            solution.append(''.join(r))
        solutions.append(solution)
        return

    # Iterate over each column in the current row
    for col in range(n):
        if is_safe(row, col, board):
            # If it's safe to place a queen in the current position
            board[row][col] = 'Q'  # Place the queen
            find_board(n, solutions, board, row + 1)  # Move to the next row recursively
            board[row][col] = '.'  # Remove the queen to explore other possibilities

if __name__ == '__main__':
    n = int(input("Enter the board size: "))
    solutions = solve_n_queens(n)

    # Print each solution and the visual representation of the chessboard
    for solution in solutions:
        for row in solution:
            for ch in row:
                print(ch, end=' ')
            print()
        print("---------------------------------------------------------------")
        print()

    print("Total possible solutions =", len(solutions))
