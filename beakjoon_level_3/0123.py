"""
네이버 부스트캠프 알고리즘 스터디: 연결 요소의 개수
https://www.acmicpc.net/problem/11724
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(n):
    visited[n] = True

    for i in range(1, a+1):
        if not visited[i] and edge[n][i]:
            dfs(i)


a, b = map(int, input().split())

edge = []
visited = []

for _ in range(a+1):
    edge.append([False]*(a+1))
    visited.append(False)

for _ in range(b):
    x, y = map(int, input().split())
    edge[x][y] = True
    edge[y][x] = True

cnt = 0
for j in range(1, a + 1):
    if not visited[j]:
        dfs(j)
        cnt += 1

print(cnt)
