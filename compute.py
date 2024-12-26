"""
2023-10-04
알고리즘 수업 - 식 계산기
"""
import re
def compute():
    print("식을 입력하세요: ")
    input_str = input()
    pattern = r'\d+|[+*]'
    string_lst = re.findall(pattern, input_str)
    add_lst = [] # 정수 리스트, 마지막에 총 합을 구할 것이다.
    range_count = 0
    for k in string_lst:
        if ord(k) == 42:
            continue
        else:
            range_count += 1
    for j in range(range_count):
        if ord(string_lst[j]) == 42: # 먼저 곱하기 기호가 나오면
            next = add_lst[-1] * int(string_lst[j + 1]) # add_lst에 있던 마지막 애와
            add_lst.pop()# 그리고 add_lst의 마지막에 들어있던 애를 pop 시키고
            add_lst.append(next)# add_lst에 next을 append한다.
            string_lst.pop(j+1)
        elif ord(string_lst[j]) == 43: # 덧셈 기호가 나왔을 때
            continue
        else:
            add_lst.append(int(string_lst[j])) # str을 정수로 변환하여 add_lst에 넣는다.
    answer = 0
    for i in add_lst:
        answer += i
    return answer

print(compute())