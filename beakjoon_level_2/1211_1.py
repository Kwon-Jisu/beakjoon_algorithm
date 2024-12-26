"""
네이버 부스트캠프 알고리즘 스터디: 수 정렬하기 2
https://www.acmicpc.net/problem/2751
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다.
이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""

import sys

n = int(sys.stdin.readline().strip())

# numbers = []
# for _ in range(n):
#     number = int(sys.stdin.readline().strip())
#     numbers.append(number)
numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]

numbers.sort()
for i in numbers:
    print(i)
