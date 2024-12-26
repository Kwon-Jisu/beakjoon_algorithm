"""
네이버 부스트캠프 알고리즘 스터디: 분해합
https://www.acmicpc.net/problem/2231
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다.
물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
"""


def de_comp(m):
    m_list = [int(i) for i in str(m)]
    return m + sum(m_list)


number = int(input())
count_up = max(1, number - len(str(number)) * 9)
# 분해합 256
# 생성자 245: 모든 생성자는 적어도 분해합 - 분해합의자릿수*9 한 것보다 크다.


while True:
    if de_comp(count_up) == number:
        print(count_up)
        break
    count_up += 1
    if count_up > number:  # 모든 탐색 끝난 경우
        print(0)
        break
