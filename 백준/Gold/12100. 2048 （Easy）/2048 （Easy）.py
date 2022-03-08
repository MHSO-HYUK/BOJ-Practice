# 12100 2048
from sys import stdin 
from copy import deepcopy
def game(cnt, m):
    global maxima
    if cnt == 5:
        maxima = max(maxima, max(map(max, m)))
        return
    else:
        for k in range(4):
            if k == 0: # 상
                maps = deepcopy(m)
                for i in range(n):
                    for j in range(n):
                        if maps[i][j]:
                            temp = i
                            while(1):
                                if temp > 0:
                                    if maps[temp-1][j] == 0:
                                        maps[temp][j], maps[temp-1][j] = maps[temp-1][j], maps[temp][j]
                                        temp = temp-1
                                    else:
                                        break
                                elif temp == 0:
                                    break
                                    
                pop = [[0 for _ in range(n)] for _ in range(n)]
                for i in range(n-1):
                    for j in range(n):
                        if maps[i][j] == maps[i+1][j] and maps[i][j]: # 위아래 결합 찾기
                            if not pop[i][j] and not pop[i+1][j]: # 겹치면 안됌
                                pop[i][j], pop[i+1][j] = 1, 1
                                maps[i][j] += maps[i][j] # 합쳐짐
                                maps[i+1][j] = 0    
                                
                for i in range(n):
                    for j in range(n):
                        if maps[i][j]:
                            temp = i
                            while(1):
                                if temp > 0:
                                    if maps[temp-1][j] == 0:
                                        maps[temp][j], maps[temp-1][j] = maps[temp-1][j], maps[temp][j]
                                        temp = temp-1
                                    else:
                                        break
                                elif temp == 0:
                                    break   
                game(cnt+1, maps)
            
            elif k == 1: # 하
                maps = deepcopy(m)
                for i in range(n-1, -1, -1):
                    for j in range(n):
                        if maps[i][j]:
                            temp = i
                            while(1):
                                if temp < n-1:
                                    if maps[temp+1][j] == 0:
                                        maps[temp][j], maps[temp+1][j] = maps[temp+1][j], maps[temp][j]
                                        temp = temp+1
                                    else:
                                        break
                                elif temp == n-1:
                                    break
            
                pop = [[0 for _ in range(n)] for _ in range(n)]
                for i in range(n-1, 0, -1):
                    for j in range(n):
                        if maps[i][j] == maps[i-1][j] and maps[i][j]: # 위아래 결합 찾기
                            if not pop[i][j] and not pop[i-1][j]: # 겹치면 안됌
                                pop[i][j], pop[i-1][j] = 1, 1
                                maps[i][j] += maps[i][j] # 합쳐짐
                                maps[i-1][j] = 0    
                                
                for i in range(n-1, -1, -1):
                    for j in range(n):
                        if maps[i][j]:
                            temp = i
                            while(1):
                                if temp < n-1:
                                    if maps[temp+1][j] == 0:
                                        maps[temp][j], maps[temp+1][j] = maps[temp+1][j], maps[temp][j]
                                        temp = temp+1
                                    else:
                                        break
                                elif temp == n-1:
                                    break
                game(cnt+1, maps)
                
            elif k == 2: # 좌
                maps = deepcopy(m)
                for j in range(n):
                    for i in range(n):
                        if maps[i][j]:
                            temp = j
                            while(1):
                                if temp > 0:
                                    if maps[i][temp-1] == 0:
                                        maps[i][temp], maps[i][temp-1] = maps[i][temp-1], maps[i][temp]
                                        temp = temp-1
                                    else:
                                        break
                                elif temp == 0:
                                    break
                pop = [[0 for _ in range(n)] for _ in range(n)]
                
                for j in range(n-1):
                    for i in range(n):
                        if maps[i][j] == maps[i][j+1] and maps[i][j]: # 위아래 결합 찾기
                            if not pop[i][j] and not pop[i][j+1]: # 겹치면 안됌
                                pop[i][j], pop[i][j+1] = 1, 1
                                maps[i][j] += maps[i][j] # 합쳐짐
                                maps[i][j+1] = 0
                                
                for j in range(n):
                    for i in range(n):
                        if maps[i][j]:
                            temp = j
                            while(1):
                                if temp > 0:
                                    if maps[i][temp-1] == 0:
                                        maps[i][temp], maps[i][temp-1] = maps[i][temp-1], maps[i][temp]
                                        temp = temp-1
                                    else:
                                        break
                                elif temp == 0:
                                    break
                game(cnt+1, maps)
            
            elif k == 3: # 우
                maps = deepcopy(m)
                for j in range(n-1, -1, -1):
                    for i in range(n):
                        if maps[i][j]:
                            temp = j
                            while(1):
                                if temp < n-1:
                                    if maps[i][temp+1] == 0:
                                        maps[i][temp], maps[i][temp+1] = maps[i][temp+1], maps[i][temp]
                                        temp = temp+1
                                    else:
                                        break
                                elif temp == n-1:
                                    break
                                    
                pop = [[0 for _ in range(n)] for _ in range(n)]
                for j in range(n-1, 0, -1):
                    for i in range(n):
                        if maps[i][j] == maps[i][j-1] and maps[i][j]: # 위아래 결합 찾기
                            if not pop[i][j] and not pop[i][j-1]: # 겹치면 안됌
                                pop[i][j], pop[i][j-1] = 1, 1
                                maps[i][j] += maps[i][j] # 합쳐짐
                                maps[i][j-1] = 0    
                                
                for j in range(n-1, -1, -1):
                    for i in range(n):
                        if maps[i][j]:
                            temp = j
                            while(1):
                                if temp < n-1:
                                    if maps[i][temp+1] == 0:
                                        maps[i][temp], maps[i][temp+1] = maps[i][temp+1], maps[i][temp]
                                        temp = temp+1
                                    else:
                                        break
                                elif temp == n-1:
                                    break
                game(cnt+1, maps)

n = int(stdin.readline())
init_maps = list(list(map(int, stdin.readline().split())) for _ in range(n))
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우 
maxima = 0
game(0, init_maps)
print(maxima)