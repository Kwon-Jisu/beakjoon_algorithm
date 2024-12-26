"""
네이버 부스트캠프 알고리즘 스터디: 제로
https://www.acmicpc.net/problem/10773
첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000) 이후 K개의 줄에 정수가 1개씩 주어진다.
정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.
재민이가 최종적으로 적어 낸 수의 합을 출력한다. 최종적으로 적어낸 수의 합은 2^31-1보다 작거나 같은 정수이다.
"""
import sys

N = int(sys.stdin.readline())

account = []
for _ in range(N):
    money = int(sys.stdin.readline().strip())
    if money == 0:
        account.pop()
    else:
        account.append(money)

print(sum(account))
