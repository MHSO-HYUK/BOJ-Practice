#1103 게임
# 보드의 가장 왼쪽 위에 [0,0] 동전 올림
from sys import stdin
import sys
sys.setrecursionlimit(10**6)

def game(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        a, b = x + maps[x][y] * dx[i], y+maps[x][y] * dy[i]
        if 0<= a <= n-1 and 0<= b <= m-1 and type(maps[a][b]) == int and cnt+1 > dp[a][b]:
            if visit[a][b]:
                print(-1)
                exit()
            else:
                dp[a][b] = cnt + 1
                visit[a][b] = True
                game(a,b,cnt+1)
                visit[a][b] = False
                
n, m = map(int, stdin.readline().split())
maps = []
for _ in range(n):
    temp = list(stdin.readline().rstrip())
    temp2 = []
    for i in temp:
        if(i != 'H'):
            temp2.append(int(i))
        else:
            temp2.append(i)
    maps.append(temp2)
dp = [[0 for _ in range(m)] for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]
dx, dy = [1,-1,0,0],[0,0,1,-1]
ans = 0

game(0,0,0)
print(ans+1)