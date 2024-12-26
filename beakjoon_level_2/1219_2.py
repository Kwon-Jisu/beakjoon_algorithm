"""
네이버 부스트캠프 알고리즘 스터디: 통계학
https://www.acmicpc.net/problem/2108
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다.
그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.
"""

import sys
from collections import Counter
import math

input = sys.stdin.readline

N = int(input())
num_lst = [int(input()) for _ in range(N)]


# 반올림 함수
def round2(num):
    return math.ceil(num) if num - math.floor(num) >= 0.5 else math.floor(num)


# 최빈값
def common(numbers):
    num_dict = Counter(numbers).most_common()
    frequencies = [frequency for _, frequency in num_dict]
    filtered = [element for element, frequency in num_dict if frequency == max(frequencies)]
    if len(filtered) == 1:
        return filtered[0]
    else:
        return sorted(filtered)[1]


print(round2(sum(num_lst) / N))
print(sorted(num_lst)[N // 2])
print(common(num_lst))
print(max(num_lst) - min(num_lst))
