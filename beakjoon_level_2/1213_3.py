"""
네이버 부스트캠프 알고리즘 스터디: 설탕 배달
https://www.acmicpc.net/problem/2839
상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
"""
import sys


n = int(sys.stdin.readline().strip())

if n % 5 == 0:
    print(n // 5)
else:
    p = 0
    while n > 0:
        n -= 3
        p += 1
        if n % 5 == 0:
            p += n // 5
            print(p)
            break
        elif n == 1 or n == 2:
            print(-1)
            break
        elif n == 0:
            print(p)
            break
