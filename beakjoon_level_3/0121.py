"""
네이버 부스트캠프 알고리즘 스터디: 나무 자르기
https://www.acmicpc.net/problem/2805
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = max(lst)
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for tree in lst:

        if tree > mid:
            cnt += tree - mid

    if cnt >= m:
        start = mid + 1
        answer = mid

    elif cnt < m:
        end = mid - 1

print(answer)
