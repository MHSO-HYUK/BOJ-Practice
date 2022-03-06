# 17822 원판 돌리기
from sys import stdin 
from collections import deque
import sys
def queueing(i, j, p):
    dx, dy= [1, -1, 0, 0], [0, 0, 1, -1]
    queue = deque([[i, j]])
    visit[i][j] = 1
    flag = False
    while(queue):
        x, y = queue.popleft()
        for k in range(4):
            a, b = x+dx[k], y+dy[k]
            if 0 <= a <= n-1 and -1 <= b <= m:
                if b == m:
                    b = 0
                if b == -1:
                    b = m-1
                if not visit[a][b] and one[a][b] == p:
                    flag = True
                    visit[a][b] = 1
                    cache[a][b] = 1
                    queue.append([a, b])
    if flag:
        cache[i][j] = 1

n, m, t = map(int, stdin.readline().split())
one = [[] for _ in range(n)]
for i in range(n):
    one[i] = list(map(int, stdin.readline().split()))
command = list(list(map(int, stdin.readline().split())) for _ in range(t))
command = command[::-1]
while(command):
    x, d, k = command.pop()
    for i in range(n):
        if not (i+1) % x:
            if d == 0: # 시계 방향 k 만큼
                one[i] = one[i][m-k:m] + one[i][0:m-k]
            if d == 1: # 반시계 방향 
                one[i] = one[i][k:m] + one[i][0:k]
    
    
    visit = [[0]*m for _ in range(n)]
    cache = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visit[i][j] and one[i][j]:
                queueing(i, j, one[i][j])
                
    k = False
    for i in range(n):
        for j in range(m):
            if cache[i][j] :
                k = True
                one[i][j] = 0 
                
    if not k : # 지워지지 않음 
        s, cnt = 0, 0
        for i in range(n):
            for j in range(m):
                if one[i][j]:
                    cnt += 1
                    s += one[i][j]
        if cnt:
            s = s / cnt
            for i in range(n):
                for j in range(m):
                    if one[i][j] > s:
                        one[i][j] -= 1
                    elif one[i][j] < s and one[i][j] != 0:
                        one[i][j] += 1
        else:
            print(sum(map(sum, one)))
            sys.exit()

print(sum(map(sum, one)))