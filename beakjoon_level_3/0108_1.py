"""
네이버 부스트캠프 알고리즘 스터디: 파도반 수열
https://www.acmicpc.net/problem/9461
"""
import sys
input = sys.stdin.readline

N = int(input())
p_list = [1, 1, 1, 2, 2]

for i in range(4, 100):
    p_list.append(p_list[i] + p_list[i - 4])

for _ in range(N):
    n = int(input())
    print(p_list[n - 1])
