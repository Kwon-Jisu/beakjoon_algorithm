"""
네이버 부스트캠프 알고리즘 스터디: 균형잡힌 세상
https://www.acmicpc.net/problem/4949
각 문자열은 마지막 글자를 제외하고 영문 알파벳, 공백, 소괄호("( )"), 대괄호("[ ]")로 이루어져 있으며, 온점(".")으로 끝나고, 길이는 100글자보다 작거나 같다.
입력의 종료조건으로 맨 마지막에 온점 하나(".")가 들어온다.
각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.
"""
import sys


def brackets(lines):
    stack = []
    for i in lines:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if not stack:
                return "no"
            elif stack[-1] == "(":
                stack.pop()
            else:
                return "no"
        elif i == "]":
            if not stack:
                return "no"
            elif stack[-1] == "[":
                stack.pop()
            else:
                return "no"
    return "yes" if not stack else "no"


answer = []
while True:
    line = sys.stdin.readline()
    if line == ".\n":
        break
    answer.append(brackets(line))

print("\n".join(answer))
