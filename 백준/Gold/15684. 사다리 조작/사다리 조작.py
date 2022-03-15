# 15684 사다리 조작
from sys import stdin
from itertools import combinations
def check():
    global g        
    for i in range(n):
        j, now = 0, i
        while(1):
            if visit[j][now] == 1:
                now += 1
            elif visit[j][now-1] == 1:
                now -= 1
            j += 1          
            if j == h:
                if now != i:
                    return 0
                break
    return 1


def ladder():
    global g
    lad = []
    for i in range(h):
        for j in range(n-1):
            if visit[i][j] == 0:
                lad.append([i, j])
    
    for i in range(4): # 사다리는 세개까지 설치해본다.
        for j in combinations(lad, i):
            for k in j:
                visit[k[0]][k[1]] = 1
            if check():
                return i
            for k in j:
                visit[k[0]][k[1]] = 0
                
    return -1

n, m, h = map(int, stdin.readline().split()) # 세로선 // 가로선 // 놓을 수 있는 위치의 갯수
garo = []
visit = [[0 for _ in range(n)] for _ in range(h)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    a, b = a-1, b-1
    if b-1 >= 0:
        visit[a][b-1] = -1
    visit[a][b] = 1
    if b+1 < n:
        visit[a][b+1] = -1
print(ladder())