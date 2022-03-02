# 14888 연산자 끼워넣기
from sys import stdin
def dfs(a, b, c, d, val, turn):
    global minima, maxima
    if turn == n:
        minima = min(minima, val)
        maxima = max(maxima, val)
        return
    else:
        if a-1 >= 0:
            dfs(a-1, b, c, d, val + num[turn], turn + 1)

        if b-1 >= 0:
            dfs(a, b-1 , c, d, val - num[turn], turn + 1)

        if c-1 >= 0:
            dfs(a, b, c-1, d, val * num[turn], turn + 1)

        if d-1 >= 0:
            dfs(a, b, c, d-1, val // num[turn] if val > 0 else -(-val//num[turn]), turn + 1)


n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
flag = list(map(int, stdin.readline().split()))
# + - * /
minima, maxima = 10**10, -10**10
dfs(flag[0], flag[1], flag[2], flag[3], num[0], 1)
print(maxima)
print(minima)




