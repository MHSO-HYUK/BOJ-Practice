#11657 타임머신
from collections import deque
from sys import stdin
def machine():
    cost[1] = 0
    global flag2
    for i in range(n):
        for j in range(m):
            a, b, c = graph[j]
            if(cost[a] != num and cost[b] > cost[a] + c):
                cost[b] = cost[a] + c
                if(i == n-1):
                    flag2 = False
                
num = 10**9
flag2 = True
n, m = map(int, stdin.readline().split())
graph = []
cost = [num for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph.append([a,b,c])
machine()
if(n == 1):
    print(-1)
else:
    if(not flag2):
        print(-1)
    else:
        for i in range(2, n+1):
            if(cost[i] == num):
                print(-1)
            else:
                print(cost[i])