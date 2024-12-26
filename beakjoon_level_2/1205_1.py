"""
네이버 부스트캠프 알고리즘 스터디: 최대 공약수와 최소 공배수
https://www.acmicpc.net/problem/2609
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
"""
import math

num1, num2 = map(int, input().split())

print(math.gcd(num1, num2))
print(math.lcm(num1, num2))