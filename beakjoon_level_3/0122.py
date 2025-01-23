"""
네이버 부스트캠프 알고리즘 스터디: 최대 힙
https://www.acmicpc.net/problem/11279
"""
import sys
input = sys.stdin.readline
import heapq

n = int(input())
max_heap = []

for _ in range(n):
    number = int(input())
    if number > 0:
        heapq.heappush(max_heap, -number)
    else:
        if not max_heap:
            print(0)
        else:
            print(-heapq.heappop(max_heap))
