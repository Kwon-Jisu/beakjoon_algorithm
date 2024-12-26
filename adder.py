"""
2023-11-08
우선 주어진 입력을 '집합'으로 만들어야 한다. -> 중복된 원소들을 제거, 1개씩만 리스트에 넣는다. -> 라이브러리가 있는지 찾아보자.
집합 리스트가 주어졌다면,
"""
# 문자열 형태의 정수를 받아 정수 타입으로 바꿔준다.
from itertools import combinations, combinations_with_replacement

def intF(n):
    return int(n)

# 사용자가 입력하는 정수 리스트 전체를 받는 함수가 필요하다.
def userSet():
    setting = input().split()
    intSet = list(map(intF, setting))  # 문자열로 받은 정수를 정수형으로 바꿔준다.
    return intSet

def setList(intSet): # 사용자로부터 받은 정수 배열 중 가장 마지막 수를 제거하고, 개수가 맞는지 체크
    intSet2 = []
    for i in intSet:
        intSet2.append(i)
    intSet2.pop()
    if (intSet2[0] == len(intSet2) - 1):
        intSet2.remove(intSet2[0])
        intSet2.sort()
        return intSet2
    else:
        return "impossible"

# 마지막 수를 리턴하는 함수
def want(intSet):
    return intSet[-1]

def sumC(n, numbers):
    answer = []
    for i in range(1, n + 1):
        for j in combinations_with_replacement(numbers, i):
            if sum(j) == n:
                answer.append(j)
    if len(answer == 0):
        return "impossible"
    else:
        return answer

intSet = userSet() # 사용자 입력 문자열(4 4 7 5 10 12)
setL = setList(intSet) # 셋 리스트(4 7 5 10 -> 4 5 7 10)
wantN = want(intSet) # 만들고자 하는 수(12)
print(sumC(wantN, setL))

