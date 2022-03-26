# 12784 인하니카 공화국
# 다리가 하나인 섬에서 1번으로 오지 못하도록 하는 최소 다이너마이트의 갯수
from sys import stdin
def inha(now):
    visit[now] = 1
    if now != 1 and len(graph[now]) == 1: # 다리가 하나인 경우
        return graph[now][0][1]
    
    temp, versus = 0, -1
    for a, b in graph[now]:
        if not visit[a]: # 자식
            temp += inha(a)
            
        else: # 부모 
            versus = b
            
    if versus != -1:
        return min(temp, versus)
    
    else:
        return temp
    
t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().split())
    graph = [[] for _ in range(1+n)]
    for _ in range(m):
        a, b, d = map(int, stdin.readline().split())
        graph[a].append([b, d])
        graph[b].append([a, d])
    visit = [0 for _ in range(1+n)]
    print(inha(1))