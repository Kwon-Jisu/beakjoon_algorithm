"""
네이버 부스트캠프 알고리즘 스터디: 최소 힙
https://www.acmicpc.net/problem/1927
"""
import heapq
import sys

input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    value = int(input())

    if not value:
        try:
            print(heapq.heappop(hq))
        except:
            print(0)
    else:
        heapq.heappush(hq, value)
