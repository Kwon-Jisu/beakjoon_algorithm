"""
네이버 부스트캠프 알고리즘 스터디: 벌집
https://www.acmicpc.net/problem/2292
위의 그림과 같이 육각형으로 이루어진 벌집이 있다.
그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다.
숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를
계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.
"""
import math


def for_bee(n):
    if n == 1:
        return 1
    elif 1 < n <= 7:
        return 2
    else:
        if math.floor((12 * n - 3)**0.5 - 9) == (12 * n - 3)**0.5 - 9:
            return int(math.floor((12 * n - 3)**0.5 - 9) // 6 + 2)
        else:
            return int(math.floor((12 * n - 3)**0.5 - 9) // 6 + 3)

# 3n**2 + 9n + 3 = N
# 3n**2 + 9n + 3 - N = 0

# 1
# 6
# 6 + 6*0
# 6 + 6*1
# 6 + 6*2
# 6(n)(n+1)/2

bee = int(input())
print(for_bee(bee))
