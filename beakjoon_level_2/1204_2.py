"""
네이버 부스트캠프 알고리즘 스터디: 팰린드롬수
https://www.acmicpc.net/problem/1259
입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 줄마다 1 이상 99999 이하의 정수가 주어진다.
입력의 마지막 줄에는 0이 주어지며, 이 줄은 문제에 포함되지 않는다.
각 줄마다 주어진 수가 팰린드롬수면 'yes', 아니면 'no'를 출력한다.
"""


def palindrome(letter):
    if len(letter) % 2 == 0:
        if letter[:len(letter)//2] == letter[len(letter)//2:][::-1]:
            return "yes"
        else:
            # print(letter[:len(letter)//2], reversed(letter[len(letter)//2:]))
            return "no"
    else:
        if letter[:len(letter)//2] == letter[len(letter)//2 + 1:][::-1]:
            return "yes"
        else:
            # print(letter[:len(letter) // 2], reversed(letter[len(letter) // 2 + 1:]))
            return "no"


num_list = []
while 1:
    num_list.append(input())
    if num_list[-1] == '0':
        num_list.pop()
        break

for i in num_list:
    print(palindrome(i))
