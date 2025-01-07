"""
네이버 부스트캠프 알고리즘 스터디: 파도반 수열
https://www.acmicpc.net/problem/11659
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
prefix_sum = [0]

temp = 0
for i in lst:
    temp += i
    prefix_sum.append(temp)

for i in range(M):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])
