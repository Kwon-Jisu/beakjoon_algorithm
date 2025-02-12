"""
네이버 부스트캠프 알고리즘 스터디: 달팽이는 올라가고 싶다
https://www.acmicpc.net/problem/2869
땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.
첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)
첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.
"""


def smail_up(up, down, tree):
    unit = up - down
    if tree <= up:
        return 1
    else:
        if (tree - up) % unit == 0:
            return (tree - up) // unit + 1
        else:
            return (tree - up) // unit + 2


up_m, down_m, tree_length = map(int, input().split())
print(smail_up(up_m, down_m, tree_length))
