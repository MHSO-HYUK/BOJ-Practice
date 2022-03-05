# 16235 나무 재테크
from sys import stdin
from collections import deque
def one():
    for i in range(n):
        for j in range(n):
            lens = len(info[i][j])
            for k in range(lens):
                if info[i][j][k] <= yang[i][j]:
                    yang[i][j] -= info[i][j][k]
                    info[i][j][k] += 1
                else:
                    for _ in range(k, lens):
                        yang[i][j] += info[i][j].pop() // 2
                    break
def two():
    for i in range(n):
        for j in range(n):
            for k in info[i][j]:
                if not k % 5:
                    for p in range(8):
                        a, b = i + dx[p], j+dy[p]
                        if 0<=a<=n-1 and 0<=b<=n-1:
                            info[a][b].appendleft(1)
            yang[i][j] += maps[i][j]

n, m, t = map(int, stdin.readline().split())
maps = list(list(map(int, stdin.readline().split())) for _ in range(n))
yang = [[5]*n for _ in range(n)]
info = [[deque() for i in range(n)] for i in range(n)]
for _ in range(m):
    r, c, age = map(int, stdin.readline().split())
    info[r-1][c-1].append(age)
dx, dy = (1,1,1,-1,-1,-1,0,0),(1,0,-1,1,0,-1,1,-1)
for _ in range(t):
    one()
    two()
      
ans = 0
for i in range(n):
    for j in range(n):
        ans +=len(info[i][j])
print(ans)