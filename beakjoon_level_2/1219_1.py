"""
네이버 부스트캠프 알고리즘 스터디: 프린터 큐
https://www.acmicpc.net/problem/1966
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.
첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.
테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다.
이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다.
중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.
각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    while queue:
        best = max(queue)  # 현재의 최댓값이 가장 먼저 배출되므로 최댓값을 저장
        front = queue.popleft() # 큐의 front를 뽑았으므로
        m -= 1 # 내 위치가 한 칸 당겨진다.

        if best == front: # 뽑은 숫자가 제일 큰 숫자일 때
            count += 1 # 하나가 영원히 배출되므로 순번 하나 추가
            if m < 0: # m이 0이라는 것은 뽑은 숫자가 내 숫자라는 뜻.
                print(count)
                break

        else:   # 뽑은 숫자가 제일 큰 숫자가 아니면
            queue.append(front) # 제일 뒤로 밀려나게 됨
            if m < 0 :  # 제일 앞에서 뽑히면
                m = len(queue) - 1 # 제일 뒤로 이동

    # while True:


    # for i in range(papers):
    #     if next(enumerate(importance))[1] == imp_idx[-1]:
    #
    #     if next(enumerate(importance))[0] == location:


