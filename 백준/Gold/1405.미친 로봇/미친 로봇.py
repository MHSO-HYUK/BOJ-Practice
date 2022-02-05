#1405 미친 로봇
#같은 곳을 한번씩만 갈 때, 단순하다고 한다.
from sys import stdin
import sys
sys.setrecursionlimit(10**6)

def robot(x, y, po, c):
    global ok
    if(c == n):
        ok += po
    else:
        for k in range(4):
            a, b = x+move[k][0][0], y+move[k][0][1]
            if(visit[a][b] == 0):
                visit[a][b] = 1
                robot(a, b, po*move[k][1], c+1)
                visit[a][b] = 0
       
n,a,b,c,d = map(int, stdin.readline().split())
maps = [[0 for _ in range(2*n+1)] for _ in range(2*n+1)]
visit = [[0 for _ in range(2*n+1)] for _ in range(2*n+1)]
move = [[[0, 1], a/100], [[0, -1],b/100], [[1, 0], c/100], [[-1, 0], d/100]]

ok = 0
visit[n][n] = 1
robot(n, n, 1,  0)
print(ok)