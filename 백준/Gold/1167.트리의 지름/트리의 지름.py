#1167 트리의 지름
from sys import stdin
from collections import deque
def tree(i):
    global temp, ans, far
    temp = max(temp, ans)
    if(temp == ans):
        far = i
        
    for v in graph[i]:
        if(visit[v[0]] == 0):
            visit[v[0]] = 1
            ans += v[1]
            tree(v[0])
            visit[v[0]] = 0
            ans -= v[1]
            
    return far

def tree2(i, j):
    global v
    queue = deque([[i, 0]])
    visit = [0 for _ in range(v+1)]
    visit[i] = 1
    while(queue):
        now, dist = queue.popleft()
        if(now == j):
            return dist
        for v in graph[now]:
            if(visit[v[0]] == 0):
                visit[v[0]] = 1
                queue.append([v[0], dist+v[1]])
        
        
v = int(stdin.readline())
graph = [[] for _ in range(v+1)]
for _ in range(v):
    idx, *p = map(int, stdin.readline().split())
    for i in range(0, len(p) - 1, 2):
        graph[idx].append([p[i], p[i+1]])
temp, ans, far =0, 0 ,0
visit = [0 for _ in range(v+1)]
visit[2] = 1
far_idx = tree(2)
temp, ans, far =0, 0 ,0
visit = [0 for _ in range(v+1)]
visit[far_idx] = 1
far_idx2 = tree(far_idx)
print(tree2(far_idx, far_idx2))