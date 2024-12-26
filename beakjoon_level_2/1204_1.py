"""
네이버 부스트캠프 알고리즘 스터디: 블랙잭
https://www.acmicpc.net/problem/15829
...
H = sum(a_i * r**i) mod M (0 <= i < l)
r = 31
M = 1234567891
이제 여러분이 할 일은 위 식을 통해 주어진 문자열의 해시 값을 계산하는 것이다. 그리고 이 함수는 간단해 보여도 자주 쓰이니까 기억해뒀다가 잘 써먹도록 하자.
첫 줄에는 문자열의 길이 L이 들어온다. 둘째 줄에는 영문 소문자로만 이루어진 문자열이 들어온다.
입력으로 주어지는 문자열은 모두 알파벳 소문자로만 구성되어 있다.
문제에서 주어진 해시함수와 입력으로 주어진 문자열을 사용해 계산한 해시 값을 정수로 출력한다.
"""


def char_to_num(letter):
    return ord(letter) - ord('a') + 1


def num_to_hash(count, n_list):
    return sum([n_list[i]*(31**i) for i in range(count)]) % 1234567891


n = int(input())
letters = input()

num_list = [char_to_num(j) for j in letters]
print(num_to_hash(n, num_list))
