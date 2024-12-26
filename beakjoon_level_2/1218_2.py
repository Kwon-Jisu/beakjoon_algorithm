"""
네이버 부스트캠프 알고리즘 스터디: solved.ac
https://www.acmicpc.net/problem/18110
아직 아무 의견이 없다면 문제의 난이도는 0으로 결정한다. 의견이 하나 이상 있다면, 문제의 난이도는 모든 사람의 난이도 의견의 30% 절사평균으로 결정한다.
제외되는 사람의 수는 위, 아래에서 각각 반올림한다. 25명이 투표한 경우 위, 아래에서 각각 3.75명을 제외해야 하는데, 이 경우 반올림해 4명씩을 제외한다.
마지막으로, 계산된 평균도 정수로 반올림된다. 절사평균이 16.7이었다면 최종 난이도는 17이 된다.
첫 번째 줄에 난이도 의견의 개수 n이 주어진다. (0 ≤ n ≤ 3 × 105)
이후 두 번째 줄부터 1 + n번째 줄까지 사용자들이 제출한 난이도 의견 n개가 한 줄에 하나씩 주어진다. 모든 난이도 의견은 1 이상 30 이하이다.
solved.ac가 계산한 문제의 난이도를 출력한다.
"""

import sys
from collections import deque
input = sys.stdin.readline


def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


N = int(input())
if N == 0:
    print(0)
else:
    tmp_lst = list(int(input().strip()) for _ in range(N))

    level_list = deque(sorted(tmp_lst))
    # print(level_list)

    percent = round2(N * 0.15)

    for _ in range(percent):
        level_list.popleft()
        level_list.pop()

    print(round2(sum(level_list) / len(level_list)))
