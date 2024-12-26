"""
네이버 부스트캠프 알고리즘 스터디: FizzBuzz
https://www.acmicpc.net/problem/28702
FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 한 줄에 하나씩 주어집니다. 각 문자열의 길이는 $8$ 이하입니다.
입력이 항상 FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열에 대응됨이 보장됩니다.
연속으로 출력된 세 개의 문자열 다음에 올 문자열을 출력하세요. 여러 문자열이 올 수 있는 경우, 아무거나 하나 출력하세요.
"""

n = 0
for i in range(3, 0, -1):
    x = input()
    if x not in ["Fizz", "Buzz", "FizzBuzz"]:
        n = int(x) + i

if not n % 3 and not n % 5:
    print("FizzBuzz")
elif not n % 3 and n % 5:
    print("Fizz")
elif n % 3 and not n % 5:
    print("Buzz")
else:
    print(n)
