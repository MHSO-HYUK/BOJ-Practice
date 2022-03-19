# 16724 피리부는 사나이 
from sys import stdin
global ans
def piri(i, j):
    global ans
    if maps[i][j] == 'U':
        a, b = i + dx[0], j + dy[0]
    elif maps[i][j] == 'D':
        a, b = i + dx[1], j + dy[1]
    elif maps[i][j] == 'L':
        a, b = i + dx[2], j + dy[2]
    elif maps[i][j] == 'R':
        a, b = i + dx[3], j + dy[3]
    
    if not visit[a][b]: # 아무도 안간 길
        visit[a][b] = ans
        check.append([a, b])
        piri(a, b) # 더 가봄
        
    elif visit[a][b] == ans: # 내가 지나갔던 길 
        ans += 1    
        return
     
    else: # 남이 지나갔던 길 
        temp = visit[a][b]
        for a, b in check:
            visit[a][b] = temp
        return

n, m = map(int, stdin.readline().split())
maps = list(list(stdin.readline().rstrip()) for _ in range(n))
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
visit = [[0 for _ in range(m)] for _ in range(n)]
ans = 1 
for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            check = [[i, j]]
            visit[i][j] = ans
            piri(i, j)
    
print(ans-1)