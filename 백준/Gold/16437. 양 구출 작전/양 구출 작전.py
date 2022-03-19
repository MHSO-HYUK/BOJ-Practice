# 16437 양 구출 작전
from sys import stdin
import sys
sys.setrecursionlimit(10**6)

def escape(node):
    sh = graph[node][1]
    for v in graph[node][2]:
        ret = escape(v)
        sh += ret
        
    if sh < 0:
        return 0
    else:
        return sh
    
n = int(stdin.readline())
graph = [[0, 0, []] for _ in range(1+n)]
bridge =  [[] for _ in range(1+n)]
for i in range(2, n+1):
    a, b, c = map(str, stdin.readline().split())
    if a == 'W':
        graph[i][0], graph[i][1] = a, -int(b)
    else:
        graph[i][0], graph[i][1] = a, int(b)
    graph[int(c)][2].append(i)
    # S 양  // b 마리 // C섬 갈 수있음
    # W 늑대 // b 마리 // C 섬 갈 수있음

print(escape(1))