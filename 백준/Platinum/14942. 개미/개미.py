# 14942 개미
# 1번 방으로 이동하고 싶다. 
# 에너지가 0이 된 개미는 더 이상 움직일 수 없다 
# 한방에서 다른 방으로 이동할 수 있는 경로는 항상 존재 + 유일 = 트리!
# i 번 방에 있던 개미가 도달할 수 있는 방 중에 1번 방과 가장 가까운 방의 번호를 출력한다. 
from sys import stdin 
def dfs(now, need):
    for b, c in graph[now]:
        if needs[b] == -1:
            parent[b] = now
            needs[b] = need + c
            dfs(b, need + c)
            
def up(now, rest_en):
    p = parent[now]
    if rest_en >= needs[now] - needs[p]:
        ret = up(p, rest_en - (needs[now] - needs[p]))
    else:
        return now
    
    return ret
    
n = int(stdin.readline())
en = [0] + list(int(stdin.readline()) for _ in range(n))
graph = [[] for _ in range(1+n)]
for _ in range(n-1):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
needs = [-1 for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
needs[1] = 0
dfs(1, 0)
for i in range(1, n+1):
    if en[i] >= needs[i]:
        print(1)
    else:
        print(up(i, en[i]))