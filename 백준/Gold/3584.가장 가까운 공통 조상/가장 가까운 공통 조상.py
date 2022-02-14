# 3584 가장 가까운 공통조상 
from sys import stdin 
from collections import deque 
def tree(a):
    parent = [a]
    queue = deque([a])
    while(queue):
        now = queue.popleft()
        for v in graph[now]:
            parent.append(v)
            queue.append(v)
    return parent


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, stdin.readline().split())
        graph[b].append(a)

    ta, tb = map(int, stdin.readline().split())
    pa = tree(ta)
    pb = tree(tb)
    flag = False
    for a in pa:
        if not flag:
            for b in pb:
                if a == b:
                    print(a)
                    flag = True
        
        else:
            break