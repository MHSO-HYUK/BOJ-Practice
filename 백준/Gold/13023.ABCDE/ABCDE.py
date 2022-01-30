#13023 ABCDE -> 신장 트리
import sys
from sys import stdin
sys.setrecursionlimit(10**6)
def tree(i):
    global f
    if(not f):
        for v in graph[i]:
            if(visit[v][1] == 0):
                visit[v][0], visit[v][1] = 1, visit[i][1] + 1
                if(visit[v][1] >= 5):
                    f = True
                tree(v)
                visit[v][1] = 0

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
  
flag, f = False, False
for i in range(n):
    visit = [[0, 0] for _ in range(n)]
    visit[i][0], visit[i][1] = 1, 1 #방문 여부 / 연결 노드 갯수
    tree(i)
    if(f):
        print(1)
        break
if(not f):
    print(0)