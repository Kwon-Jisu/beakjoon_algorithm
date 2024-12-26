def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, n):
    # Base case: If all queens are placed
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_n_queens(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, then remove queen from board[i][col]
            board[i][col] = 0  # BACKTRACK

    # If the queen cannot be placed in any row in this column, then return false
    return False

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0, n):
        # Format the board for a more readable output
        formatted_board = []
        for row in board:
            formatted_row = "".join(['Q' if cell == 1 else '_' for cell in row])
            formatted_board.append(formatted_row)
        return formatted_board
    else:
        return "No solution"

# Example usage
n_queens_solution = n_queens(5)
print(n_queens_solution)

