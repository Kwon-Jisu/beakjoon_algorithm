"""
네이버 부스트캠프 알고리즘 스터디: 잃어버린 괄호
https://www.acmicpc.net/problem/1541
"""
import sys
input = sys.stdin.readline

n = input()
m = n.split('-')

answer = 0
x = sum(map(int, (m[0].split('+'))))
if n[0] == '-':
    answer -= x
else:
    answer += x

for x in m[1:]:
    x = sum(map(int, (x.split('+'))))
    answer -= x
print(answer)
