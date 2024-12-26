import sys


def counting_sort():
    # 1. 입력 처리: 모든 입력을 읽어서 리스트로 분리
    data = sys.stdin.read().split()

    # 2. 카운팅 배열 생성: 수의 범위는 1 ~ 10,000
    counts = [0] * 10001

    # 3. 입력 데이터를 순회하며 카운팅
    for num in data:
        counts[int(num)] += 1

    # 4. 카운팅 결과를 기반으로 정렬된 결과 출력
    output = sys.stdout
    for num in range(1, 10001):
        if counts[num] > 0:
            output.write((str(num) + '\n') * counts[num])

# 실행을 위해 이 함수를 호출하십시오.
counting_sort()

