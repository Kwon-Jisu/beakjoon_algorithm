"""
네이버 부스트캠프 알고리즘 스터디: 체스판 다시 칠하기
https://www.acmicpc.net/problem/1018
지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다. 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
"""
import sys

M, N = map(int, sys.stdin.readline().split())
old_chess = ""
for _ in range(M):
    old_chess += sys.stdin.readline().strip()


# 문자열에서 모든 줄바꿈 문자를 제거합니다.
def remove_newlines(input_string):
    return input_string.replace('\n', '')


# 두 문자열의 같은 위치에서 서로 다른 문자의 개수를 반환합니다.
def count_differences(str1, str2):
    return sum(1 for a, b in zip(str1, str2) if a != b)


old_chess = remove_newlines(old_chess)
black = \
    "BWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB"
white = \
    "WBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW"

black = remove_newlines(black)
white = remove_newlines(white)

min_error = 64
for m_count in range(M - 8 + 1):
    for n_count in range(N - 8 + 1):
        unit = ""
        for i in range(8):
            unit += old_chess[m_count*N + n_count + i*N: m_count*N + n_count + i*N + 8]
        if min(count_differences(unit, black), count_differences(unit, white)) < min_error:
            min_error = min(count_differences(unit, black), count_differences(unit, white))

# print(min_error)

# import sys
#
# M, N = map(int, sys.stdin.readline().split())
# old_chess = [sys.stdin.readline().strip() for _ in range(M)]
#
#
# # 두 체스판의 차이를 계산
# def calculate_error(board, start_row, start_col, color):
#     error = 0
#     for i in range(8):
#         for j in range(8):
#             expected = 'B' if (i + j) % 2 == (0 if color == 'B' else 1) else 'W'
#             if board[start_row + i][start_col + j] != expected:
#                 error += 1
#     return error
#
#
# min_error = 64  # 최악의 경우는 8x8에서 모두 다른 경우
#
# # 슬라이딩 윈도우 방식으로 8x8 체스판 탐색
# for m in range(M - 7):  # M-8+1과 동일
#     for n in range(N - 7):  # N-8+1과 동일
#         black_error = calculate_error(old_chess, m, n, 'B')
#         white_error = calculate_error(old_chess, m, n, 'W')
#         min_error = min(min_error, black_error, white_error)
#
# print(min_error)
