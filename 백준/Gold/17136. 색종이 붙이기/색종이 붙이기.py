# 17136 색종이 붙이기
from sys import stdin
import sys
def check(nxt, a, b, c, d, e):
    global minima, visit
    
    if search[nxt] == [0, 0]:
        if visit[0][0]:
            pass
        else:
            if maps[0][0]:
                if a < 5:
                    a += 1
                else:
                    return
        minima = min(minima, a+b+c+d+e)
        return
   
    if a+b+c+d+e > minima:
        return
    
    if a > 5 or b > 5 or c >5 or d > 5 or e > 5:
        return
    
    x, y = search[nxt]
    if maps[x][y] and not visit[x][y]:
        k = dp[x][y]
        for size in range(5, 0, -1):
            if size <= k:
                temp = []
                flag = True
                if size == 1:
                    if a < 5:
                        visit[x][y] = 1
                        check(nxt+1, a+1, b, c, d, e)
                        visit[x][y] = 0
                        
                if size == 2:
                    if b < 5:
                        for p in range(x-1, x+1):
                            for q in range(y-1, y+1):
                                if visit[p][q]:
                                    flag = False
                                else:
                                    temp.append([p, q])
                                    visit[p][q] = 1
                        if flag:
                            check(nxt+1, a, b+1, c, d, e)
                        for p, q in temp:
                            visit[p][q] = 0
                if size == 3:
                    if c < 5:
                        for p in range(x-2, x+1):
                            for q in range(y-2, y+1):
                                if visit[p][q]:
                                    flag = False
                                else:
                                    temp.append([p, q])
                                    visit[p][q] = 1
                        if flag:
                            check(nxt+1, a, b, c+1, d, e)
                        for p, q in temp:
                            visit[p][q] = 0
                if size == 4:
                    if d < 5:
                        for p in range(x-3, x+1):
                            for q in range(y-3, y+1):
                                if visit[p][q]:
                                    flag = False
                                else:
                                    temp.append([p, q])
                                    visit[p][q] = 1
                        if flag:
                            check(nxt+1, a, b, c, d+1, e)
                        for p, q in temp:
                            visit[p][q] = 0
                if size == 5:
                    if e < 5:
                        for p in range(x-4, x+1):
                            for q in range(y-4, y+1):
                                if visit[p][q]:
                                    flag = False
                                else:
                                    temp.append([p, q])
                                    visit[p][q] = 1
                        if flag:
                            check(nxt+1, a, b, c, d, e+1)
                        for p, q in temp:
                            visit[p][q] = 0
    
    else:
        check(nxt+1, a, b, c, d, e)
                        
search = []
for i in range(9, -1, -1):
    for j in range(9, -1, -1):
        search.append([i, j])

maps = list(list(map(int, stdin.readline().split()))for _ in range(10))
dp = [[0]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        if maps[i][j]:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
minima = 100
visit = [[0]*10 for _ in range(10)]
check(0, 0, 0, 0, 0, 0)
if minima == 100:
    print(-1)
else: print(minima)