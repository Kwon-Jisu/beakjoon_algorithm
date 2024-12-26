"""
네이버 부스트캠프 알고리즘 스터디: 큐
https://www.acmicpc.net/problem/10845

"""

import sys

queue = []
n = int(sys.stdin.readline())

for i in range(n):
    cm = sys.stdin.readline().split()
    if cm[0] == 'push':
        queue.append(cm[1])
    elif cm[0] == "front":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])
    elif cm[0] == "back":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[-1])
    elif cm[0] == 'size':
        print(len(queue))
    elif cm[0] == 'empty':
        if len(queue) == 0:
            print("1")
        else:
            print("0")
    elif cm[0] == 'pop':
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.pop(0))
