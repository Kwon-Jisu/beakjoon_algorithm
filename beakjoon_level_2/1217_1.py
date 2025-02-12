"""
네이버 부스트캠프 알고리즘 스터디: 숫자카드2
https://www.acmicpc.net/problem/10816
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며,
이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
"""

import sys

N = int(sys.stdin.readline().strip())
N_s = sorted(list(map(int, sys.stdin.readline().strip().split())))
M = int(sys.stdin.readline().strip())
M_s = list(map(int, sys.stdin.readline().strip().split()))

n_dic = {}
for n in N_s:
    if n in n_dic:
        n_dic[n] += 1
    else:
        n_dic[n] = 1


def binary(m, N_s, start, end):
    if start > end:
        return 0
    mid = (start + end)//2
    if m == N_s[mid]:
        return n_dic[m]
    elif m < N_s[mid]:
        return binary(m, N_s, start, mid-1)
    else:
        return binary(m, N_s, mid+1, end)


for m in M_s:
    print(binary(m, N_s, 0, len(N_s)-1), end=' ')
