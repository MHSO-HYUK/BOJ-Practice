# 1033 칵테일
# 재료가 모두 정수가 되면서 총 질량은 모두 0보다 커야함
# 이때 질량을 모두 더한 값이 최소가 되어야 한다.
from sys import stdin
from copy import deepcopy
def gcd(a, b):
    while(b):
        a, b = b, a%b
    return a

def lcm(a, b):
    return (a*b) // gcd(a, b)

def dfs(now):
    global ans
    visit[now] = 1
    for a, p, q in graph[now]:
        if not visit[a]:
            j, m = ans[now]
            ans[a] = [j*q, m*p]
            dfs(a)
                         
n = int(stdin.readline())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, p, q = map(int, stdin.readline().split()) # q * a = p * b
    graph[a].append([b, p, q])
    graph[b].append([a, q, p])
    
visit = [0 for _ in range(n)]
ans = [[1, 1] for _ in range(n)]

for i in range(n):
    if not visit[i]:
        dfs(i)

for i in range(n):
    a, b = ans[i][0], ans[i][1]
    g = gcd(a, b)
    ans[i][0], ans[i][1] = ans[i][0] // g , ans[i][1] // g

temp = []
for i in range(n):
    temp.append(ans[i][1])
l = temp[0]
for i in range(1,n):
    l = lcm(l, temp[i])

for i in range(n):
    print((l*ans[i][0]) // ans[i][1], end = ' ')