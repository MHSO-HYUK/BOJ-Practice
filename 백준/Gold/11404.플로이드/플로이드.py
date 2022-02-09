#11404 플로이드
from sys import stdin
def floyd():
    global INF
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if(i != j and graph[i][j] > graph[i][k] + graph[k][j]):
                    graph[i][j] = graph[i][k] + graph[k][j]
INF = 10**10
n, m = int(stdin.readline()), int(stdin.readline())
graph = [[INF]*(n+1) for _ in range(n+1)]
visit = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    if(not graph[a][b]):
        graph[a][b] = c
    else:
        graph[a][b] = min(graph[a][b], c)

floyd()
for i in range(1, n+1):
    for j in range(1, n+1):
        if(graph[i][j] == INF):
            print(0, end = ' ')
        else:
            print(graph[i][j], end = ' ')
    print()