"""
네이버 부스트캠프 알고리즘 스터디: 소수 구하기
https://www.acmicpc.net/problem/1929
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
"""

import sys
input = sys.stdin.readline


def sieve_of_eratosthenes(m, n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    # 에라토스테네스의 체로 소수 판별
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(m, n + 1) if is_prime[i]]


M, N = map(int, input().split())
primes = sieve_of_eratosthenes(M, N)

# 출력
print('\n'.join(map(str, primes)))

# import sys
# input = sys.stdin.readline
#
# M, N = map(int, input().split())
#
#
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# numbers = list(i for i in range(M, N + 1))
#
# answer = []
# for n in numbers:
#     if is_prime(n):
#         answer.append(n)
#
# print('\n'.join(map(str, answer)))
