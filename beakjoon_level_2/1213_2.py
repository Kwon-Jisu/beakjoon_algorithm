"""
네이버 부스트캠프 알고리즘 스터디: 카드2
https://www.acmicpc.net/problem/2164
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.
"""
from collections import deque

# 입력 처리
import sys
N = int(sys.stdin.readline().strip())

n_deque = deque(range(1, N + 1))

button = False

while len(n_deque) > 1:
    if button:
        n_deque.append(n_deque.popleft())
        button = False
    else:
        n_deque.popleft()
        button = True

print(n_deque[0])

# import sys
#
#
# N = int(sys.stdin.readline().strip())
#
# n_lst = list(i + 1 for i in range(N))
# # print(n_list)
#
# button = False
#
# while len(n_lst) != 1:
#     if button is True:
#         alive = n_lst.pop(0)
#         n_lst.append(alive)
#         button = False
#     else:
#         alive = n_lst.pop(0)
#         button = True
#
# print(n_lst[0])
