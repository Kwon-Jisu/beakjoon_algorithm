"""
네이버 부스트캠프 알고리즘 스터디: 피보나치 함수
https://www.acmicpc.net/problem/9095
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
"""
import sys
input = sys.stdin.readline


def func(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return func(x - 1) + func(x - 2) + func(x - 3)


t = int(input())
for _ in range(t):
    n = int(input())
    print(func(n))
