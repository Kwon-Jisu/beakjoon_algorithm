"""
네이버 부스트캠프 알고리즘 스터디: 스택
https://www.acmicpc.net/problem/10828

"""
import sys
input = sys.stdin.readline

stack = []
N = int(input())

for i in range(N):
    order = input().split()
    if order[0] == 'push':   # 정수를 stack에 넣기
        stack.append(order[1])
    if order[0] == 'pop':    # 가장 위에 있는(나중에 들어온) 정수를 빼고 출력
        if len(stack) != 0:
            print(stack[-1])
            stack.pop()
        else:   # 스택이 비어있다면 -1을 출력
            print(-1)
    if order[0] == 'size':   # 스택에 들어 있는 정수의 개수 출력
        print(len(stack))
    if order[0] == 'empty':   # 스택이 비어있으면 1, 아니면 0 출력
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if order[0] == 'top':   # 스택의 가장 위에 있는 정수를 출력
        if len(stack) != 0:
            print(stack[-1])
        else:   # 스택이 비어있다면 -1을 출력
            print(-1)
