"""
네이버 부스트캠프 알고리즘 스터디: 평균
https://www.acmicpc.net/problem/1546
첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다. 둘째 줄에 세준이의 현재 성적이 주어진다.
이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.
첫째 줄에 새로운 평균을 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.
"""


def new_mean(count, subjects):
    mean = sum([i/max(subjects)*100 for i in subjects]) / count
    return mean


n = int(input())
n_list = list(map(int, input().split()))

print(new_mean(n, n_list))