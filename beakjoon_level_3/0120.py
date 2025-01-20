import sys
input = sys.stdin.readline

n = int(input())
B = [list(map(int, input().split())) for _ in range(n)]
w_cnt, b_cnt = 0, 0


def div_conq(x, y, m):
    global w_cnt, b_cnt
    tmp_cnt = 0
    for i in range(x, x + m):
        for j in range(y, y + m):
            if B[i][j]:
                tmp_cnt += 1
    if not tmp_cnt:
        w_cnt += 1
    elif tmp_cnt == m**2:
        b_cnt += 1
    else:
        div_conq(x, y, m // 2)
        div_conq(x + m // 2, y, m // 2)
        div_conq(x, y + m // 2, m // 2)
        div_conq(x + m // 2, y + m // 2, m // 2)
    return


div_conq(0, 0, n)
print(w_cnt)
print(b_cnt)
