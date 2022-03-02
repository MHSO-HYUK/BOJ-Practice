# 17140 이차원 배열과 연산
# 행 연산 -> 행 >= 열일때 적용
# 열 연산 -> 열 > 행일때 적용
from sys import stdin
from copy import deepcopy

n, m, k = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(3)]
cnt = 0
while(1):
    if cnt > 100:
        print(-1)
        break
        
    if len(maps) > 100:
        maps = maps[0:100]
        
    if len(maps[0]) > 100:
        for i in range(len(maps)):
           maps[i] = maps[i][0:100]
    
    
    if len(maps) >= n and len(maps[0]) >= m and maps[n-1][m-1] == k:
        print(cnt)
        break
    
        
    else:
        p, q = len(maps), len(maps[0])
        if p >= q: # 행 >= 열 (R 연산)
            for i in range(p):
                temp = dict(([i, 0] for i in range(101)))
                slist = []
                for j in range(q):
                    temp[maps[i][j]] += 1
                for z in range(1, 101):
                    if temp[z]:
                        slist.append([z, temp[z]])
                slist.sort(key = lambda x : x[1])
                maps[i] = []
                for x in range(len(slist)):
                    for y in range(len(slist[x])):
                        maps[i].append(slist[x][y])       
            maxima = 0
            for i in range(p):
                maxima = max(maxima, len(maps[i]))
            for i in range(p):
                for _ in range(maxima-len(maps[i])):
                    maps[i].append(0)    
            cnt += 1   
        
        else: # 행 < 열 (C 연산)    
            flag = 0
            n_maps = [[] for _ in range(100)] 
            for i in range(q):
                temp = dict(([i, 0] for i in range(101)))
                slist = []
                for j in range(p):
                    temp[maps[j][i]] += 1 

                for z in range(1, 101):
                    if temp[z]:
                        slist.append([z, temp[z]])
                flag = max(flag, len(slist))
                
                
                slist.sort(key = lambda x : x[1])

                flag = 0
                for x in range(len(slist)):
                    for y in range(len(slist[x])):
                        n_maps[flag].append(slist[x][y])
                        flag += 1
                
                for x in range(flag, 100):
                    n_maps[x].append(0)

            for i in range(len(n_maps)):
                if sum(n_maps[i]) == 0:
                    q = i
                    break
            n_maps = n_maps[0:i]
            maxima = 0
            for i in range(len(n_maps)):
                maxima = max(maxima, len(n_maps[i]))
            for i in range(len(n_maps)):
                for _ in range(maxima-len(n_maps[i])):
                    n_maps[i].append(0)           
            maps = deepcopy(n_maps)
            
            cnt += 1