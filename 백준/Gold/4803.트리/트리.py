#4803 트리
#트리의 갯수를 찾는 문제 (사이클이 존재하지 않아야 한다.)
from sys import stdin
from collections import deque
def tree(i):
    global tree_num
    queue = deque([i])
    flag = False
    while(queue):
        node = queue.popleft()
        visit[node] = tree_num
        for v in graph[node]:
            if node == v:
                istree[node] = 0
                flag = True
            
            if visit[v] == 0:
                if parent[v] == parent[node]:
                    flag = True

                elif parent[v] > parent[node]:
                    temp = parent[v]
                    for p in range(1, n+1):
                        if(parent[p] == temp):
                            parent[p] = parent[node]
                    queue.append(v)

                elif parent[v] < parent[node]:
                    temp = parent[node]
                    for p in range(1, n+1):
                        if(parent[p] == temp):
                            parent[p] = parent[v]
                    queue.append(v)
    
    if flag:
        for i in range(1, n+1):
            if(parent[i] == parent[node]):
                istree[i] = 0
        tree_num -= 1   
num = 1
while(1):
    n, m = map(int, stdin.readline().split()) 
    if([n,m] == [0, 0]):
        break
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        
    visit = [0 for _ in range(n+1)]
    
    parent = [i for i in range(n+1)]
    
    istree = [1 for _ in range(n+1)]
    
    tree_num = 0
    for i in range(1, n+1):
        if visit[i] == 0:
            tree_num += 1
            tree(i)

    if sum(istree) == 1:
        print(f'Case {num}: No trees.')
        
    elif tree_num == 1:
        print(f'Case {num}: There is one tree.')
    
    else:
        print(f'Case {num}: A forest of {tree_num} trees.')

    num += 1