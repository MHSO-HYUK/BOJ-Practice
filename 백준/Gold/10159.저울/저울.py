#10159 저울
from sys import stdin
def compare():
    for v in graph:
        
        for k in v[0]: #나보다 작은 놈에겐는 내 부모를 준다.
            a = set(graph[k][1])
            a.update(v[1])
            graph[k][1] = list(a)
        for k in v[1]: #나보다 큰놈에게는 내 자식을 준다.
            a = set(graph[k][0])
            a.update(v[0])
            graph[k][0] = list(a)

n, m = int(stdin.readline()), int(stdin.readline())
graph = [[[],[]] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][1].append(b)
    graph[b][0].append(a)
compare()
for i in range(1, n+1):
    print(n-1-len(graph[i][0])-len(graph[i][1]))