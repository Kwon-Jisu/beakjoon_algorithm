"""
네이버 부스트캠프 알고리즘 스터디: 피보나치 함수
https://www.acmicpc.net/problem/1003
다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
"""
import sys
input = sys.stdin.readline

N = int(input())
input_lst = list(int(input()) for _ in range(N))

fib_lst = [[0, 0] for _ in range(max(2, max(input_lst) + 1))]

fib_lst[0] = [1, 0]
fib_lst[1] = [0, 1]

for n in range(2, len(fib_lst)):
    fib_lst[n] = [a + b for a, b in zip(fib_lst[n-1], fib_lst[n-2])]

for j in input_lst:
    print(fib_lst[j][0], fib_lst[j][1])
