"""
네이버 부스트캠프 알고리즘 스터디: 패션왕 신해빈
https://www.acmicpc.net/problem/9375
첫째 줄에 테스트 케이스가 주어진다. 테스트 케이스는 최대 100이다.
각 테스트 케이스의 첫째 줄에는 해빈이가 가진 의상의 수 n(0 ≤ n ≤ 30)이 주어진다.
다음 n개에는 해빈이가 가진 의상의 이름과 의상의 종류가 공백으로 구분되어 주어진다. 같은 종류의 의상은 하나만 입을 수 있다.
모든 문자열은 1이상 20이하의 알파벳 소문자로 이루어져있으며 같은 이름을 가진 의상은 존재하지 않는다.
각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로 의상을 입을 수 있는 경우를 출력하시오.
"""
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    wears = {}
    for j in range(n):
        wear = list(input().split())
        if wear[1] in wears:
            wears[wear[1]].append(wear[0])
        else:
            wears[wear[1]] = [wear[0]]

    cnt = 1  # 각 종류마다 항목의 개수

    for k in wears:
        cnt *= (len(wears[k]) + 1)
    print(cnt-1)
