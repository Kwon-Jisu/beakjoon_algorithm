"""
네이버 부스트캠프 알고리즘 스터디: 소수 찾기
https://www.acmicpc.net/problem/1978
"""

N = int(input())
num_list = list(map(int, input().split()))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


answer = sum(1 for num in num_list if is_prime(num))

print(answer)
