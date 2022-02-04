#1058 친구
from collections import deque
from sys import stdin
def friend(i):
    num = []
    queue = deque([[i, 0]])
    while(queue):
        a, b = queue.popleft()
        if(b > 1):
            break
        for v in graph[a]:
            if(not v in num and v != i):
                num.append(v)
                queue.append([v, b+1])
    return len(num)

n = int(stdin.readline())
graph = [[] for _ in range(n+1)]
for i in range(n):
    maps = list(stdin.readline().rstrip())
    for j in range(n):
        if maps[j] == 'Y':
            graph[i].append(j)
maxima = 0
for i in range(n):
    maxima = max(maxima, friend(i))
print(maxima)