"""
*** 네이버 부스트캠프 알고리즘 스터디: 단어 정렬 ***
https://www.acmicpc.net/problem/1181
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
<길이가 짧은 것부터, 길이가 같으면 사전 순으로> 단, 중복된 단어는 하나만 남기고 제거해야 한다.
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000)
둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.
"""

# append와 insert 유의하기 -> 좀 더 찾아보기
count = int(input())
# words = [list(set([input() for _ in range(count)])), []]
# count = len(words[0])
#
# while True:
#     if len(words[1]) == 0:
#         words[1].append(words[0].pop())
#     elif len(words[1]) == count:
#         break
#     else:
#         word_0 = words[0].pop()
#         inserted = False
#         for i in range(len(words[1])):
#             if len(word_0) < len(words[1][i]):
#                 words[1].insert(i, word_0)
#                 inserted = True
#                 break
#             elif len(word_0) == len(words[1][i]):
#                 if word_0 < words[1][i]:
#                     words[1].insert(i, word_0)
#                     inserted = True
#                     break
#         if not inserted:
#             words[1].append(word_0)
words = sorted(set(input() for _ in range(count)), key=lambda x: (len(x), x))

print("\n".join(words))
