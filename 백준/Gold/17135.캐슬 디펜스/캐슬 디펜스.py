#17135 캐슬 디펜스
# 0 : 빈칸 1 : 적//궁수 세명  N+1 행 배치//거리=x+ y//
# 제일 가까운 놈 공격 + 여러명이면 젤 왼쪽 공격
# 공격 받으면 제외 // 공격 끝나면 적은 한칸 아래로 
from copy import deepcopy
from sys import stdin
def castle(a,b,c):
    global n
    temp = [a,b,c]
    flag, flag2 = 0, False
    ans = []
    maps = deepcopy(mapp)
    cnt = 0
    while(flag != n+1):
        visit = [[[0, 0, 0] for _ in range(m)] for _ in range(n)] # a/b/c 거리
        kill = [[0 for _ in range(m)] for _ in range(n)]
        enemy = [[] for _ in range(3)]
        #거리 측정 (궁수 셋에 대한)
        for k in range(3):
            minima = 10**6
            flag3 = False
            for j in range(m):    
                for i in range(n-1, -1, -1):
                    if(maps[i][j] == 1):
                        visit[i][j][k] = abs(i-n)+abs(j-temp[k]) 
                        if(visit[i][j][k] <= d and visit[i][j][k] < minima):
                            minima = visit[i][j][k] # 가장 가까운 적을 죽여야 + 가장 왼쪽 
                            tempi, tempj = i,j 
                            flag3 = True
            if(flag3):
                enemy[k] = [[tempi, tempj]]         
            
        # 궁수가 죽일 적 선정
        for k in range(3):
            for p, q in enemy[k]:
                kill[p][q] = 1
                maps[p][q] = 0
        # 죽이고 다음 턴으로
        for i in range(n-1, 0, -1):
            for j in range(m):
                if(kill[i][j] == 1):
                    cnt += 1
                maps[i][j] = maps[i-1][j]
        maps[0] = [0]*m
        flag += 1
        ans.append(cnt)
    return max(ans)
        
n,m,d = map(int, stdin.readline().split()) # d: 공격 거리 제한 
mapp = []
for _ in range(n):
    mapp.append(list(map(int, stdin.readline().split())))
    
defend = []
for i in range(0, m-2):
    for j in range(i+1, m-1):
        for k in range(j+1, m):
            defend.append([i,j,k])
ans = []
for a, b, c in defend:
    ans.append(castle(a,b,c))
print(max(ans))