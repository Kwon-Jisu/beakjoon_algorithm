"""
네이버 부스트캠프 알고리즘 스터디: 부녀회장이 될 테야
https://www.acmicpc.net/problem/2775
이 아파트에 거주를 하려면 조건이 있는데, “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다”
는 계약 조항을 꼭 지키고 들어와야 한다.
아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.
단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다.
각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.
"""

count = int(input())
floors = []
rooms = []
for i in range(count):
    floors.append(int(input()))
    rooms.append(int(input()))
max_f = max(floors)
max_r = max(rooms)

dp = [[0] * (max_r + 1) for _ in range(max_f + 1)]
for n in range(1, max_r + 1):
    dp[0][n] = n

for f in range(1, max_f + 1):
    for r in range(1, max_r + 1):
        dp[f][r] = dp[f - 1][r] + dp[f][r - 1]

print(dp)

for j in range(count):
    print(dp[floors[j]][rooms[j]])

# T = int(input())
#
# for t in range(T):
#     k = int(input())
#     n = int(input())
#
#     apt = [[0 for i in range(n)] for j in range(k+1)]
#     apt[0] = [b+1 for b in range(n)]
#
#     for a in range(1,k+1):
#         for b in range(n):
#             apt[a][b] = sum(apt[a-1][:b+1])
#
#     print(f"{t+1}번 apt: {apt}")
#     print(apt[k][n-1])