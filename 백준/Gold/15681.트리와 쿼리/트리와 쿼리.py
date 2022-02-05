#15681 트리와 쿼리
# u를 루트로 할때 서브트리에 속한 정점의 수!
from sys import stdin
from collections import deque
def tree(i):
    queue = deque([i])
    visit[i] = 1
    while(queue):
        root = queue.popleft()
        for v in graph[root]:
            if(visit[v] == 0):
                visit[v] = 1
                relation[v][1] = root
                relation[root][0].append(v)
                queue.append(v)
    
    degree = []
    for i in range(n+1):
        degree.append(len(relation[i][0]))
    queue = deque()
    for i in range(1, n+1):
        if(degree[i] == 0):
            dp[i] = 1
            queue.append(i)
    while(queue):
        son = queue.popleft()
        if(degree[relation[son][1]] > 0):
            dp[relation[son][1]] += dp[son]
            degree[relation[son][1]] -= 1
            if(degree[relation[son][1]] == 0):
                queue.append(relation[son][1])
        
n, r, q = map(int, stdin.readline().split()) #r: 루트
graph = [[] for _ in range(n+1)]
relation = [[[], 0] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

quest = []
for _ in range(q):
    quest.append(int(stdin.readline()))
dp = [1 for _ in range(n+1)] 
visit = [0 for _ in range(n+1)]
tree(r)
for k in range(q):
    print(dp[quest[k]])