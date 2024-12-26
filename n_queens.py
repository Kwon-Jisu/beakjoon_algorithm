"""
2023-12-26 알고리즘: N-Queen problem
N-Queen 문제는 N이라는 자연수 (3이상)의 수를 입력 받아  NxN 짜리 크기의 체스판에 N개의 Queen을 배치하는 방법을 찾는 문제입니다.
Queen은 상,하,좌.우, 대각선의 방향으로 움직여 상대 말을 잡는 것이 가능합니다.
N개의 queen은 서로 잡을 수 없도록 배치하는 문제입니다.
입력: 3 이상의 정수 N (<20)
출력: 서로 잡을 수 없는 queen의 배치(1개)와 가능한 모든 조합의 수
Ex) 입력: 4
_Q__
___Q
Q___
__Q_
2
또는 입력: 3
0
"""
def test(board, row, col, n):
    # 왼쪽부터 확인
    for i in range(col):
        if board[row][i] == 1:
            return False
    # 윗쪽 확인
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # 아랫쪽 확인
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def setting(board, col, n, solutions):
    # 모든 퀸들이 배치 완료
    if col >= n:
        solutions.append([row[:] for row in board])
        return
    # 열 확인
    for i in range(n):
        if test(board, i, col, n):
            # board[i][col]에 퀸 배치
            board[i][col] = 1

            setting(board, col + 1, n, solutions)
            # 백트레킹
            board[i][col] = 0

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    setting(board, 0, n, solutions)

    return solutions

def format_solutions(all_solutions):
    # 1을 Q으로, 0을 _으로 교체
    formatted_all_solutions = []
    for solution in all_solutions:
        formatted_solution = [" ".join(['Q' if cell == 1 else '_' for cell in row]) for row in solution]
        formatted_all_solutions.append(formatted_solution)
    print("\n".join(str(item) for item in formatted_solution))
    return

#
def n_queens_formatted(n):
    solutions = n_queens(n)
    if len(solutions) == 0:
        return 0
    else:
        format_solutions(solutions)
        return len(solutions)

print(n_queens_formatted(3))