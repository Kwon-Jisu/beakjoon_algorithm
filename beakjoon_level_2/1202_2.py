"""
네이버 부스트캠프 알고리즘 스터디: 웰컴 키트
https://www.acmicpc.net/problem/30802
"""

N = int(input())
shirts = list(map(int, input().split()))
pair_t, pair_p = map(int, input().split())

total_t = 0

for shirt in shirts:
    if shirt % pair_t == 0:
        total_t += shirt // pair_t
    else:
        total_t += (shirt // pair_t) + 1

print(total_t)
print(N // pair_p, N % pair_p)
