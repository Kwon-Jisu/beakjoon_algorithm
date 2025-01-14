"""
https://www.acmicpc.net/problem/17626
"""
import sys
input = sys.stdin.readline

N = int(input())
sq = [0 if i**0.5%1 else 1 for i in range(N + 1)]

count = 4
for i in range(int(N ** 0.5), 0, -1):
    if sq[N]:
        count = 1
        break
    elif sq[N - i ** 2]:
        count = 2
        break
    else:
        for j in range(int((N - i ** 2) ** 0.5), 0, -1):
            if sq[(N - i ** 2) - j ** 2]:
                count = 3
print(count)
