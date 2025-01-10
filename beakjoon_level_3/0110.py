"""
https://www.acmicpc.net/problem/17626
"""
import sys
input = sys.stdin.readline

N = int(input())
sq = [0 if i**0.5%1 else 1 for i in range(N + 1)]  # 제곱수는 1로 저장

count = 4
for i in range(int(N ** 0.5), 0, -1):
    if sq[N]:  # n이 제곱수일 경우
        count = 1
        break
    elif sq[N - i ** 2]:  # 나머지가 제곱수일 경우
        count = 2
        break
    else:
        for j in range(int((N - i ** 2) ** 0.5), 0, -1):
            if sq[(N - i ** 2) - j ** 2]:  # 제곱수를 한번 더 뺀 나머지가 제곱수일 경우
                count = 3
print(count)
