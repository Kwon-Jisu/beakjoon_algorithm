"""
네이버 부스트캠프 알고리즘 스터디: 직각삼각형
https://www.acmicpc.net/problem/4153
"""


def right_tri(num_list):
    max_n = max(num_list)
    num_list.remove(max_n)

    if max_n ** 2 == num_list[0] ** 2 + num_list[1] ** 2:
        return "right"
    else:
        return "wrong"


all_lists = []  # 전체 리스트를 저장할 리스트

while True:
    line = input()
    numbers = list(map(int, line.split()))  # 한 줄의 숫자를 리스트로 변환
    if numbers == [0, 0, 0]:  # 종료 조건
        break
    all_lists.append(numbers)  # 변환한 리스트를 추가

for n_list in all_lists:
    print(right_tri(n_list))