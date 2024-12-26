"""
네이버 부스트캠프 알고리즘 스터디: 나는야 포켓몬 마스터 이다솜
https://www.acmicpc.net/problem/1620
"""
import sys
input = sys.stdin.readline


n, m = map(int, input().strip().split())
by_id = {}
by_name = {}
for i in range(1, n + 1):
    pokemon = input().strip()
    by_id[i] = pokemon
    by_name[pokemon] = i

for _ in range(m):
    x = input().strip()
    if x.isdigit():
        print(by_id[int(x)])
    else:
        print(by_name[x])
