#2660 회장뽑기
from collections import deque
from sys import stdin
def chairman():
    for i in range(1, n+1):
        queue = deque([[i, -1]])
        temp = set([i])
        cnt = 0
        while(len(temp) != n):
            while(queue):
                k, c = queue.popleft()
                for v in graph[k]:
                    if(not v in temp):
                        visit[i][c+1].add(v)
                        queue.append([v, c+1])
                        temp.add(v)
           

n = int(stdin.readline())
graph = [[] for _ in range(n+1)]
while(1):
    a, b = map(int , stdin.readline().split())
    if(a==-1 and b == -1):
        break
    graph[a].append(b)
    graph[b].append(a)
    
visit = [[set() for _ in range(50)]for _ in range(n+1)]
chairman()

score = [0 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(49, -1,-1):
        if len(visit[i][j]):
            score[i] = j+1
            break

minima = 10**10
for i in range(1, n+1):
    if(minima>score[i]):
        chair = [i]
        minima = score[i]
    elif(minima == score[i]):
        chair.append(i)
        
print(minima, len(chair))
for i in range(len(chair)):
    print(chair[i], end = ' ')