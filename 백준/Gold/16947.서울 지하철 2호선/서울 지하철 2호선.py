#16947 서울 지하철 2호선 
# 1. 사이클을 구하기
# 2. 각 노드의 사이클까지의 거리 구하기 
from sys import stdin
import sys
sys.setrecursionlimit(10**5)
def subway(a):
    global flag, temp
    for v in graph[a]:
        if visit[v] == 0 and not v in cycle and not flag:
            visit[v] = 1
            cycle.append(v)
            subway(v)
            if flag:
                return cycle, temp
            visit[v] = 0
            cycle.remove(v)
            
            
        if v in cycle and v != cycle[-2]:
            temp = v
            flag = True
            
            

def way(a):
    global ans, flag
    for v in graph[a]: 
        if visit[v] == 0 and not v in cycles and not flag:
            visit[v] = 1
            ans += 1
            way(v)
            if flag:
                return ans
            visit[v] = 0
            ans -= 1
            
        if v in cycles:
            ans += 1
            flag = True
    
n = int(stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

    

visit = [0 for _ in range(n+1)]
flag = False
cycle, visit[1] = [1], 1
temp = 0

cycles, v = subway(1)
for i in range(len(cycles)):
    if cycles[i] == v:
        temp = i
        break
cycles = cycles[temp:]


for i in range(1, n+1):
    if i in cycles:
        print(0, end = ' ')
    else:
        visit = [0 for _ in range(n+1)]
        visit[i] = 1
        ans, flag = 0, False
        way(i)
        print(ans, end = ' ')


