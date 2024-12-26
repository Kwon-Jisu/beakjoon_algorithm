"""
네이버 부스트캠프 알고리즘 스터디: 팩토리얼 0의 개수
https://www.acmicpc.net/problem/1676
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
첫째 줄에 구한 0의 개수를 출력한다.
"""
import math

n = math.factorial(int(input()))

num = 0

while True:
    if n % 2 == 0 and n % 5 == 0:
        num += 1
        n = n // 10
    else:
        break

print(num)
