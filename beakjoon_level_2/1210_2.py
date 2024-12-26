"""
네이버 부스트캠프 알고리즘 스터디: 영화감독 숌
https://www.acmicpc.net/problem/1436
종말의 수란 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수를 말한다.
제일 작은 종말의 수는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 이다.
따라서, 숌은 첫 번째 영화의 제목은 "세상의 종말 666", 두 번째 영화의 제목은 "세상의 종말 1666"와 같이 이름을 지을 것이다.
일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 수) 와 같다.
"""

import re

n = int(input())
least = 666

while True:
    if '666' in re.split(r'(666)', str(least)):
        # print(re.split(r'(666)', str(least)))
        n -= 1
        if n == 0:
            print(least)
            break
        else:
            least += 1
    else:
        # print(re.split(r'(666)', str(least)))
        least += 1
