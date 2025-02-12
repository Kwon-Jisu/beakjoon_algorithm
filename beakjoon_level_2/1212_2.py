"""
네이버 부스트캠프 알고리즘 스터디: 좌표 정렬하기 2
https://www.acmicpc.net/problem/11651
2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000)
좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
"""

import sys


N = int(sys.stdin.readline().strip())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for lst in points:
    tmp = lst[0]
    lst[0] = lst[1]
    lst[1] = tmp

for y, x in sorted(points):
    print(x, y)
