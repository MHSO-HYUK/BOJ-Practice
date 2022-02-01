# 2250 트리의 높이와 너비
from sys import stdin
from collections import deque
def tree(x): # x : 루트노드
    level[x] = 1
    queue = deque([[x, 1]])
    while(queue):
        node, l = queue.popleft() 
        a, b = graph[node][1][0], graph[node][1][1]
        if(a != -1 and b != -1): #자식이 둘
            level[a],level[b] = l+1, l+1
            queue.append([a, level[a]])
            queue.append([b, level[b]])
        if(a != -1 and b == -1): #왼쪽 자식만 존재
            level[a] = l+1
            queue.append([a, level[a]])
        if(a == -1 and b != -1): #오른쪽 자식만 존재
            level[b] = l+1
            queue.append([b, level[b]])
def cm(x):
    flag = False
    v = graph[x][1]  
    if(visit[v[0]] == 0): # 왼쪽 자식 미방문시
        cm(v[0])

    if(visit[v[0]] == 1 and visit[v[1]] == 0): #왼쪽 자식 방문시 + 오른쪽 미방문
        temp.append(x)
        visit[x] = 1
        cm(v[1])
    
    if(visit[v[0]] == 1 and visit[v[1]] == 1 and visit[x] == 0): #둘다 방문 
        temp.append(x)
        visit[x] = 1

n = int(stdin.readline())
graph = [[-1,[]] for _ in range(n+1)] # 부모노드 / 자식노드
visit = [0 for _ in range(n+1)]
visit[0] = 1
graph[0][1] = [-1, -1]
for i in range(n):
    a, b, c = map(int , stdin.readline().split())
    if(b == -1):
        b = 0
    if(c == -1):
        c = 0
    graph[a][1] = [b, c]
    graph[b][0], graph[c][0] = a, a
temp = []
level = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if(graph[i][0] == -1):
        tree(i)
        cm(i)
        
idx = [[] for _ in range(n+1)]
for a in range(n):
    idx[level[temp[a]]].append(a+1)
for a in range(n):
    if(idx[a]):
        idx[a] = max(idx[a]) - min(idx[a]) + 1

ans, maxima = 1, 1
for a in range(n):
    if(idx[a]):
        if(maxima < idx[a]):
            ans = a
            maxima = idx[a]

print(ans, maxima, end = ' ')